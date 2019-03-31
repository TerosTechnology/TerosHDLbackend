const shell = require('shelljs');
const fs    = require('fs')
const pkg   = require('../package.json');

// The path to the directory to copy the file(s) to.
const DEST_DIR = './build';

// NOTE: `customField` below should be replaced with the
// actual key name in the final `package.json`.
const srcFilePaths = pkg.src;

// Create a new destination directory and intermediate
// directories if necessary.
if (!shell.test('-d', DEST_DIR)) {
  shell.mkdir('-p', DEST_DIR);
}

// Recursively copy each file listed in the `customField` Array.
// Logs and error if the file listed cannot be found.
srcFilePaths.forEach(function (srcPath) {
  if (!shell.test('-e', srcPath)) {
    shell.echo('Error: Cannot find file listed in package.json: %s', srcPath);
    process.exit(1);
  }
  if(fs.lstatSync(srcPath).isFile() == true){
    shell.cp(srcPath, DEST_DIR);
  }
  else{
    var walk = function(dir) {
        var results = [];
        var list = fs.readdirSync(dir);
        list.forEach(function(file) {
            file = dir + '/' + file;
            var stat = fs.statSync(file);
            if (stat && stat.isDirectory()) {
                /* Recurse into a subdirectory */
                results = results.concat(walk(file));
            } else {
                /* Is a file */
                if (fs.lstatSync(file).isFile() == true){
                    shell.cp(file, DEST_DIR);
                }
            }
        });
        return results;
    }
    walk(srcPath)
  }
});
