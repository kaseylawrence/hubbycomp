# hubbycomp
HubbyComp is a simple application for troubleshooting demultiplexing issues with sequencing data. The app runs locally, once built with pyinstaller on target os to create an executable. The main feature is to generate reverse complement of index sequence and secondarily checks a sqlite database for known indexes. This could help figure out what indexes were used for library prep and if the correct orientation was used for demux.

Currently in the sequences.db sqlite database:
IDT-ILMN Nextera DNA UD Indexes Sets A-D

I plan to add more indexes to the database and features over time.

dependencies:
customtkinter
sqlite3



<img width="396" alt="image" src="https://github.com/kaseylawrence/hubbycomp/assets/1130770/6ed07c65-0917-4a1c-8873-d86f42717623">

