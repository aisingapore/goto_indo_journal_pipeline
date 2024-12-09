EXCLUDED_PDF_PATHS = [
    # OCR result is not good.
    '/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/1131-2174-2-PB_1.pdf',
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/1559-3195-1-SM_1.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/2093-4647-1-SM_1.pdf",

    # Not a paper (mostly table of content and list of editorial team of the journal).
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/1165-71-PB.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/1165-75-PB.pd",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/1165-77-PB.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/1222-222-PB.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/20853-Article Text-41475-2-10-20180514.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/20859-Article Text-41489-2-10-20180514.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/20862-Article Text-41504-2-10-20180514.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/20867-Article Text-41519-2-10-20180514.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/23636-Article Text-50057-2-10-20230502.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/2564-720-PB.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/26962-Article Text-78760-1-10-20190825.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/27229-Article Text-59772-2-10-20190204.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/27231-Article Text-59775-1-10-20181117.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/28761-Article Text-65065-1-10-20190209.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/28964-Article Text-72043-1-10-20190628.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/34101-Article Text-80348-1-10-20190918.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/34811-Article Text-121578-1-10-20210228.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/35605-Article Text-85235-1-10-20191120.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/37-1-PB_1.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/37-1-PB.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/37970-Article Text-93079-1-10-20200312.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/38787-Article Text-96782-1-10-20200526.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/39106-Article Text-97951-1-10-20200618.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/40950-Article Text-105144-1-10-20200919.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/51476-Article Text-144608-1-10-20211101.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/55800-Article Text-159640-1-10-20220329.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/568-1502-1-SM_1.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/568-1502-1-SM.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/607-1717-1-SM_1.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/607-1717-1-SM.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/63799-Article Text-184789-1-10-20221222.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/712-2122-1-PB_1.pdf",
    "/home/ubuntu/us-south-fs/indo-journal-pipeline/indo_journals_subsets/subset_2/712-2122-1-PB.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/1342-271-PB_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/1343-283-PB_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/14714-42869-1-SP_1.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/14714-42871-1-SP.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/1560-319-PB_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/18646-45333-1-SM_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/18647-45335-1-SM_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/18648-45337-1-SM_1.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/18652-45343-1-SM_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/24568-61027-1-SM_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/24592-61087-1-SM_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/26754-80074-1-SM.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/28874-62614-1-SM.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/3892-11715-1-SP.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/529-49-PB_2.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/5308-16932-2-SP_1.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/635-2415-1-SP.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/678-71-PB_1.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/678-72-PB_1.pdf",
    "/home/ubuntu/us-west-3-fs/indo-journal-pipeline/indo_journals_subsets/subset_3/921-132-PB_2.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1131-196-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1131-225-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1202-218-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1202-224-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1203-234-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1342-271-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1343-283-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/1528-302-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/17394-42256-1-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/18646-45333-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/18647-45335-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/18648-45337-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/18652-45343-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/24568-61027-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/24592-61087-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/456-51-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/456-52-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/47134-Article Text-129019-1-10-20210605.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/47147-Article Text-129124-1-10-20210606.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/47163-Article Text-129167-2-10-20210606.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/529-48-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/529-49-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/54440-Article Text-154492-1-10-20220203.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/573-45-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/573-46-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/64376-Article Text-186312-1-10-20230103.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/662-931-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/675-957-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/678-71-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/678-72-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/770-1231-1-SM.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/771-87-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/771-88-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/921-131-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/921-132-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/996-166-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/996-167-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/999-187-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_1/999-226-PB.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/11424-33246-1-SP.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/17423-54099-1-PB_1.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/19403-60169-1-PB_1.pdf",
    "/home/ubuntu/west-filesys/indo-journal-pipeline/indo_journals_subsets/subset_4/624-160-PB.pdf",

    # Cannot be converted to HTML (no error, function never returns).
    "/shared/gojek/extracted-pdf-marker-chunk/raw_extracted/chunk_6/Perwali_2018_55/Perwali_2018_55.md",
    "/shared/gojek/extracted-pdf-marker-chunk/raw_extracted/chunk_7/PERBUB NO. 30 TAHUN 2016 ttg Standar Satuan Harga Umum Kab.Boalemo/PERBUB NO. 30 TAHUN 2016 ttg Standar Satuan Harga Umum Kab.Boalemo.md",
    "/shared/gojek/extracted-pdf-marker-chunk/raw_extracted/chunk_0/Peraturan BPOM Nomor 29 Tahun 2021/Peraturan BPOM Nomor 29 Tahun 2021.md",
    "/shared/gojek/extracted-pdf-marker-chunk/raw_extracted/chunk_0/Peraturan Kepala BPOM Nomor 8 Tahun 2016/Peraturan Kepala BPOM Nomor 8 Tahun 2016.md",
    "/shared/gojek/extracted-pdf-marker-chunk/raw_extracted/chunk_5/PMK Nomor 103 Tahun 2018/PMK Nomor 103 Tahun 2018.md",
    "/shared/gojek/extracted-pdf-marker-chunk/raw_extracted/chunk_5/PMK Nomor 241 Tahun 2010_compressed/PMK Nomor 241 Tahun 2010_compressed.md",
]
