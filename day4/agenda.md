# Speed up CPU bound tasks

- [x] Multiple Threads
- [x] Multiple processes

# IO Bound tasks
- [ ] reading from disk
- [ ] reading from network
- [ ] getting data from a sensor (USB)

-----------------

Thread(target=download_file_1).start()
Thread(target=download_file_2).start()

------------------

at the same time(download_file_1 AND download_file_2)

------------------


