package main

import (
	"io/ioutil"
	"net/http"
	"runtime"
	"strconv"
	"testing"
)

func TestMain(t *testing.T) {
	runtime.GOMAXPROCS(2)
    go main()
	count := 3000
	procs := 10
	c := make(chan bool, count)
	for i := 0; i < procs; i++ {
		go func() {
			for j := 0; j < count/procs; j++ {
				resp, err := http.Get("http://127.0.0.1:8080/increase")
				if err != nil {
					t.Errorf("http error %s", err)
					c <- false
				} else {
					resp.Body.Close()
					c <- true
				}
			}
		}()
	}

	errCount := 0

	for i := 0; i < count; i++ {
		if !<-c {
			errCount += 1
		}
	}

	t.Logf("response fail %d", errCount)

	resp, err := http.Get("http://127.0.0.1:8080/")
	if err != nil {
		t.Fatalf("%s", err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		t.Fatalf("%s", err)
	}
	if string(body) != strconv.Itoa(count) {
		t.Fatalf("expect %d actual %s", count, string(body))
	}
}
