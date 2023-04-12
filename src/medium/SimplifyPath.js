/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function (path) {
    let stack = [];
    let pathParts = path.split('/');

    for (let i = 0; i < pathParts.length; i++) {
        if (pathParts[i] === "" || pathParts[i] === ".") {
            continue;
        }

        if (pathParts[i] === "..") {
            stack.pop();
            continue;
        }

        stack.push(pathParts[i]);
    }

    let canonicalPath = stack.join("/");
    return "/" + canonicalPath
};