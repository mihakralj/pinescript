#!/usr/bin/env node

import { readFileSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';

// Get all subdirectories in indicators folder
const getSubdirs = () => readdirSync('indicators', { withFileTypes: true })
  .filter(dirent => dirent.isDirectory())
  .map(dirent => dirent.name);

// Extract links from a table row
const extractLink = row => {
  const match = row.match(/\[([^\]]+)\]\(([^)]+)\)/);
  return match ? { symbol: match[1], path: match[2] } : null;
};

// Extract first markdown table from content
const extractTable = content => {
  const tableMatch = content.match(/\|[^\n]*\|[\s\S]*?(?=\n\n|\n$|$)/);
  return tableMatch ? tableMatch[0] : null;
};

// Process each _index.md file
const processIndexFiles = () => {
  const subdirs = getSubdirs();
  const stats = {};
  const implemented = {};

  for (const dir of subdirs) {
    try {
      const indexPath = join('indicators', dir, '_index.md');
      const content = readFileSync(indexPath, 'utf8');
      const table = extractTable(content);
      if (table) {
        // Get table rows (skip header and separator)
        const rows = table.split('\n').slice(2).filter(row => row.trim());
        const total = rows.length;
        let implCount = 0;
        implemented[dir] = [];

        // Process each row
        for (const row of rows) {
          const link = extractLink(row);
          if (link) {
            const basePath = link.path.replace('/indicators/', '').replace('.md', '');
            const mdPath = join('indicators', basePath + '.md');
            const pinePath = join('indicators', basePath + '.pine');

            if (existsSync(mdPath) && existsSync(pinePath)) {
              implCount++;
              implemented[dir].push(link.symbol);
            }
          }
        }

        stats[dir] = {
          total,
          implemented: implCount,
          unimplemented: total - implCount
        };
      }
    } catch (err) {
      if (err.code !== 'ENOENT') {
        console.error(`Error processing ${dir}:`, err.message);
      }
    }
  }

  // Print implemented indicators
  console.log('\nImplemented Indicators by Directory:');
  console.log('=================================');
  for (const [dir, symbols] of Object.entries(implemented)) {
    if (symbols.length > 0) {
      console.log(`\n${dir.toUpperCase()} (${symbols.length}):`);
      console.log(symbols.join(', '));
    }
  }

  // Print statistics
  console.log('\n\nDirectory Statistics (implemented + unimplemented = total):');
  console.log('------------------------------------------------');
  let totalImplemented = 0;
  let grandTotal = 0;

  for (const [dir, stat] of Object.entries(stats)) {
    console.log(`${dir.padEnd(15)} ${stat.implemented} + ${stat.unimplemented} = ${stat.total}`);
    totalImplemented += stat.implemented;
    grandTotal += stat.total;
  }

  console.log('------------------------------------------------');
  console.log(`TOTAL${' '.repeat(10)} ${totalImplemented} + ${grandTotal - totalImplemented} = ${grandTotal}`);
};

processIndexFiles();
