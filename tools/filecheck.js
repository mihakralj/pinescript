#!/usr/bin/env node

const fs = require('fs').promises;
const path = require('path');

const validateMdLink = (content, mdFile) => {
  const linkMatch = content.match(/\[Pine Script Implementation of .*?\]\((https:\/\/github\.com\/[^\s\)]+\.pine)\)/i);
  if (!linkMatch) return 'Missing or invalid Pine Script implementation link';

  const link = linkMatch[1];
  const expectedPath = mdFile.replace(/\.md$/, '.pine').replace(/\\/g, '/');
  const expectedLink = `https://github.com/mihakralj/pinescript/blob/main/${expectedPath}`;

  return link === expectedLink ? null : `Invalid link:\nFound:    ${link}\nExpected: ${expectedLink}`;
};

const validatePineLink = (content, pineFile) => {
  const docMatch = content.match(/\/\/@doc\s+(https:\/\/github\.com\/[^\s]+\.md)/m);
  if (!docMatch) return 'Missing //@doc link';

  const link = docMatch[1].trim();
  const expectedPath = pineFile.replace(/^indicators/, 'indicators').replace(/\\/g, '/');
  const expectedLink = `https://github.com/mihakralj/pinescript/blob/main/${expectedPath.replace('.pine', '.md')}`;

  return link === expectedLink ? null : `Invalid link:\nFound:    ${link}\nExpected: ${expectedLink}`;
};

const findFiles = async (dir, ext) => {
  const results = [];
  const items = await fs.readdir(dir, { withFileTypes: true });

  for (const item of items) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory() && !item.name.startsWith('.')) {
      results.push(...await findFiles(fullPath, ext));
    } else if (item.name.endsWith(ext)) {
      results.push(fullPath);
    }
  }
  return results;
};

(async () => {
  try {
    const pineFiles = await findFiles('indicators', '.pine');
    const mdFiles = await findFiles('indicators', '.md');
    const errors = [];

    // Check .pine files
    for (const pineFile of pineFiles) {
      const content = await fs.readFile(pineFile, 'utf8');
      const error = validatePineLink(content, pineFile);
      if (error) {
        errors.push(`${pineFile}:\n${error}\n`);
      }
    }

    // Check .md files
    for (const mdFile of mdFiles) {
      if (mdFile.endsWith('_index.md')) continue; // Skip index files
      const content = await fs.readFile(mdFile, 'utf8');
      const error = validateMdLink(content, mdFile);
      if (error) {
        errors.push(`${mdFile}:\n${error}\n`);
      }
    }

    if (errors.length) {
      console.log('\nDocumentation link errors found:');
      errors.forEach(err => console.log(err));
    } else {
      console.log('\nAll files have correct bidirectional links');
    }
  } catch (err) {
    console.error('Error:', err.message);
    process.exit(1);
  }
})();
