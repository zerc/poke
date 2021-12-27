package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

func ServeFile(prefix string, w http.ResponseWriter, r *http.Request)  {
	name := strings.Replace(r.URL.Path, prefix, "", 1)
	name = strings.Split(name, "/")[0]
	name = strings.Split(name, ".")[0]
	fname := fmt.Sprintf("mocks/%s_%s.json", strings.ToLower(r.Method), name)

	http.ServeFile(w, r, fname)
	w.Header().Add("Content-Type", "applicaiton/json")
}

func MainHandler(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Path
	log.Printf("[info] serving %s", path)

	prefixes := []string{"/pokeapi/pokemon-species/", "/translate/"}
	for _, prefix := range prefixes {
		if strings.HasPrefix(path, prefix) {
			ServeFile(prefix, w, r)
			return
		}
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
