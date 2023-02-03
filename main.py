import speedtest

kb = 1000

test = speedtest.Speedtest()

print("Testing download speed...")
download = test.download()

print("Testing upload speed...")
upload = test.upload()

print("Download speed:", (download/kb)/kb, "Upload speed:", (upload/kb)/kb, "MBPS")
