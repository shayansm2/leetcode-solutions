package main

func generateParenthesis(n int) []string {
	return recursiveParenthesisGenerator("", n, 0, 0)
}

func recursiveParenthesisGenerator(soFar string, n, openCount, closeCount int) []string {
	if openCount == n && openCount-closeCount == 0 {
		return []string{soFar}
	}

	if openCount == n {
		return recursiveParenthesisGenerator(soFar+")", n, openCount, closeCount+1)
	}

	if openCount-closeCount == 0 {
		return recursiveParenthesisGenerator(soFar+"(", n, openCount+1, closeCount)
	}

	return append(
		recursiveParenthesisGenerator(soFar+")", n, openCount, closeCount+1),
		recursiveParenthesisGenerator(soFar+"(", n, openCount+1, closeCount)...,
	)
}
