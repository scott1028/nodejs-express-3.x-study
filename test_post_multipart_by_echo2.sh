{
    echo -e "POST /upload/ HTTP/1.1\nHost: 127.0.0.1:3000\nContent-Length: 132\nContent-Type: multipart/form-data; boundary=abcd\n\n--abcd\nContent-Disposition: form-data; name=\"input_file\"; filename=\"TestFile.log\"\nContent-Type: text/x-log\n\ntest\n--abcd--\n";
    sleep 1;
} | nc 127.0.0.1 3000
