const fs = require('fs');
const path = require('path');

function extractIndicatorInfo(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const match = content.match(/indicator\((["'])(.*?)\1,\s*(["'])(.*?)\3/);
    if (match) {
        return {
            fullName: match[2],
            codeName: match[4]
        };
    }
    return null;
}

function findPineFiles(dir, baseDir) {
    const files = fs.readdirSync(dir);
    let pineFiles = [];

    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            pineFiles = pineFiles.concat(findPineFiles(fullPath, baseDir));
        } else if (path.extname(file) === '.pine') {
            const relativePath = path.relative(baseDir, fullPath);
            const info = extractIndicatorInfo(fullPath);
            if (info) {
                pineFiles.push({
                    path: relativePath,
                    ...info
                });
            }
        }
    }
    return pineFiles;
}

const indicatorsDir = path.join(__dirname, '..', 'indicators');
const pineFiles = findPineFiles(indicatorsDir, path.join(__dirname, '..', 'indicators'));

pineFiles
    .sort((a, b) => a.path.localeCompare(b.path))
    .forEach((file, i) => {
        const num = (i + 1).toString().padStart(3, ' ');
        console.log(`${num}. ${file.path.padEnd(30)} ${file.fullName.padEnd(45)} ${file.codeName}`);
    });
