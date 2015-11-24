{
    echo -e "POST /upload/ HTTP/1.1\r";
    echo -e "Host: 127.0.0.1:3000\r";
    echo -e "Content-Length: 128\r";
    echo -e "Content-Type: multipart/form-data; boundary=abcd\r";
    echo -e "\r";
    echo -e "--abcd\r";
    echo -e "Content-Disposition: form-data; name=\"input_file\"; filename=\"TestFile.log\"\r";
    echo -e "Content-Type: text/x-log\r";
    echo -e "\r";
    echo -e "test12\r";
    echo -e "--abcd--\r";
    sleep 1;
} | nc 127.0.0.1 3000