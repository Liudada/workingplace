package main

import (
	"fmt"
	"net/http"
)

var num int = 0

func show(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%d", num)
}

func add(w http.ResponseWriter, r *http.Request) {
	num = num + 1
}

func main() {
	http.HandleFunc("/", show)
	http.HandleFunc("/increase/", add)
	http.ListenAndServe(":8080", nil)
}
