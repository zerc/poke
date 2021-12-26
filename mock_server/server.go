package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

func MainHandler(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Path

	if strings.HasPrefix(path, "/pokeapi/pokemon-species/") && r.Method == "GET" {
		name := strings.Replace(r.URL.Path, "/pokeapi/pokemon-species/", "", 1)
		name = strings.Split(name, "/")[0]
		fname := fmt.Sprintf("mocks/%s.json", name)
		log.Printf("[info] serving %s", fname)
		http.ServeFile(w, r, fname)
		w.Header().Add("Content-Type", "applicaiton/json")
		return
	} 

	http.Error(w, "Not found", http.StatusNotFound)
}

func main() {
	host_port := os.Getenv("HOST_PORT")
	if host_port == "" {
		host_port = "127.0.0.1:8080"
	}

	http.HandleFunc("/", MainHandler)
	fmt.Printf("Starting mock server at %s\n", host_port)
	log.Fatal(http.ListenAndServe(host_port, nil))
}
