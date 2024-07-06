package main

import "fmt"

type WordDictionaryTrie struct {
	root *TrieTreeNode
}

type TrieTreeNode map[int32]*TrieTreeNode

func WordDictionaryTrieConstructor() WordDictionaryTrie {
	return WordDictionaryTrie{root: &TrieTreeNode{}}
}

func (this *WordDictionaryTrie) AddWord(word string) {
	node := this.root
	for _, char := range word {
		if _, found := (*node)[char]; !found {
			(*node)[char] = &TrieTreeNode{}
		}
		node = (*node)[char]
	}
	(*node)['#'] = nil
}

func (this *WordDictionaryTrie) Search(word string) bool {
	return recursiveSearch(word, this.root)
}

func recursiveSearch(word string, startNode *TrieTreeNode) bool {
	node := startNode
	for i, char := range word {
		if node == nil {
			return false
		}

		if string(char) == "." {
			for _, nextNode := range *node {
				if recursiveSearch(word[i+1:], nextNode) {
					return true
				}
			}
			return false
		}

		if _, found := (*node)[char]; !found {
			return false
		}
		node = (*node)[char]
	}
	if node == nil {
		return false
	}
	_, found := (*node)['#']
	return found
}

func main() {
	wordDictionary := WordDictionaryTrieConstructor()
	wordDictionary.AddWord("bad")
	wordDictionary.AddWord("dad")
	wordDictionary.AddWord("mad")
	fmt.Println(wordDictionary.Search("pad")) // return False
	fmt.Println(wordDictionary.Search("bad")) // return True
	fmt.Println(wordDictionary.Search(".ad")) // return True
	fmt.Println(wordDictionary.Search("b..")) // return True
}
