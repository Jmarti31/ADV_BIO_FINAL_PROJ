##Edited ENTRY MIG000004 & MIG000005 in PGADMIn4 for disease, replaced . with ' ###

DROP TABLE IF EXISTS interactions;
CREATE TABLE interactions
(
    Interaction_ID	VARCHAR(11) PRIMARY KEY,
    miRBase_ID	VARCHAR(20),
    Directionality	VARCHAR(10),
    Organism_Name	VARCHAR(150),
    Effects	TEXT[],
    Disease_Name	VARCHAR(150),
    DOI_ID	VARCHAR(512),
    PMID	INTEGER
);

INSERT INTO interactions (Interaction_ID,miRBase_ID,Directionality,Organism_Name,Effects,Disease_Name,DOI_ID,PMID)
VALUES
    ('MIG000001', 'hsa-mir-155-1', '->', 'Fusobacterium nucleatum', '{Increased Proliferation, Disease Decrease}', 'Colitis', '10.1016/j.chom.2015.12.005', '26764595'),
    ('MIG000002', 'hsa-mir-1226', '->', 'Escherichia coli', '{Increased Proliferation, Disease Decrease}', 'Colitis', '10.1016/j.chom.2015.12.005', '26764595'),
    ('MIG000003', 'has-mir-139', '->', 'Blautia', '{Increased Proliferation, Disease Decrease}', 'Colorectal Cancer', '10.1128/mSystems.00205-17', '29795787'),
    ('MIG000004', 'hsa-let-7b', '<-', 'Escherichia coli O83:H1 str. NRG 857C', '{Decreased Expression, TLR4 Over Expression, Disease Increase}', 'Crohn.s Disease', '10.1016/j.bcp.2018.08.029', '30142321'),
    ('MIG000005', 'hsa-mir-146', '<-', 'Herpes simplex virus-1', '{Increased Expression, NF-KB Activation, Disease Increase}', 'Alzheimer.s Disease', '10.3389/fneur.2018.00145', '29615954'),
    ('MIG000006', 'hsa-mir-223', '<-', 'Escherichia coli Nissle 1917', '{Decreased Expression, IL-1B Under Expression, Disease Decrease}', 'Colitis', '10.3389/fphar.2018.00468', '29867475'),
    ('MIG000007', 'hsa-mir-155', '<-', 'Escherichia coli Nissle 1917', '{Decreased Expression, IL-1B Under Expression, IL-12 Under Expression, TGF-β Over Expression, Disease Decrease}', 'Colitis', '10.3389/fphar.2018.00468', '29867475'),
    ('MIG000008', 'hsa-mir-150', '<-', 'Escherichia coli Nissle 1917', '{Decreased Expression, c-Myb Under Expression, Disease Decrease}', 'Colitis', '10.3389/fphar.2018.00468', '29867475'),
    ('MIG000009', 'hsa-mir-143', '<-', 'Escherichia coli Nissle 1917', '{Increased Expression, Disease Decrease}', 'Colitis', '10.3389/fphar.2018.00468', '29867475'),
    ('MIG000010', 'hsa-mir-375', '<-', 'Escherichia coli Nissle 1917', '{Increased Expression, Disease Decrease}', 'Colitis', '10.3389/fphar.2018.00468', '29867475'),
    ('MIG000011', 'hsa-mir-223', '<-', 'Saccharomyces boulardii', '{Decreased Expression, Disease Decrease}', 'Colitis', '10.1016/j.jnutbio.2018.08.005', '30236870'),
    ('MIG000012', 'hsa-mir-155', '<-', 'Saccharomyces boulardii', '{Decreased Expression, IL-1B Under Expression, TGF-β Over Expression, Disease Decrease}', 'Colitis', '10.1016/j.jnutbio.2018.08.005', '30236870'),
    ('MIG000013', 'hsa-mir-150', '<-', 'Lactobacillus fermentum', '{Decreased Expression, Disease Decrease}', 'Colitis', '10.1002/mnfr.201700144', '28752563'),
    ('MIG000014', 'hsa-mir-155', '<-', 'Lactobacillus fermentum', '{Decreased Expression, Disease Decrease}', 'Colitis', '10.1002/mnfr.201700144', '28752563'),
    ('MIG000015', 'hsa-mir-223', '<-', 'Lactobacillus fermentum', '{Decreased Expression, Disease Decrease}', 'Colitis', '10.1002/mnfr.201700144', '28752563'),
    ('MIG000016', 'hsa-mir-143', '<-', 'Lactobacillus fermentum', '{Increased Expression, Disease Decrease}', 'Colitis', '10.1002/mnfr.201700144', '28752563'),
    ('MIG000017', 'hsa-mir-155', '<-', 'Lactobacillus salivarius', '{Decreased Expression, Disease Decrease}', 'Colitis', '10.1002/mnfr.201700144', '28752563'),
    ('MIG000018', 'hsa-mir-223', '<-', 'Lactobacillus salivarius', '{Decreased Expression, Disease Decrease}', 'Colitis', '10.1002/mnfr.201700144', '28752563'),
    ('MIG000019', 'hsa-mir-143', '<-', 'Listeria monocytogenes', '{Decreased Expression, Disease Increase}', 'Listeriosis', '10.1128/mBio.00707-13', '24327339'),
    ('MIG000020', 'hsa-mir-148a', '<-', 'Listeria monocytogenes', '{Decreased Expression, Disease Increase}', 'Listeriosis', '10.1128/mBio.00707-13', '24327339'),
    ('MIG000021', 'hsa-mir-200b', '<-', 'Listeria monocytogenes', '{Decreased Expression, Disease Increase}', 'Listeriosis', '10.1128/mBio.00707-13', '24327339'),
    ('MIG000022', 'hsa-mir-200c', '<-', 'Listeria monocytogenes', '{Decreased Expression, Disease Increase}', 'Listeriosis', '10.1128/mBio.00707-13', '24327339'),
    ('MIG000023', 'hsa-mir-21', '<-', 'Fusobacterium nucleatum', '{Increased Expression,  TLR4 Activation, MYD88 Activation, NF-KB Activation, RASA1 Under Expression, Disease Increase}', 'Colorectal Cancer', '10.1053/j.gastro.2016.11.018', '27876571'),
    ('MIG000024', 'hsa-mir-135b', '<-', 'Lactobacillus acidophilus', '{Decreased Expression, KRAS Over Expression, Disease Decrease}', 'Colon Cancer', '10.1007/s12602-018-9478-8', '30311185'),
    ('MIG000025', 'hsa-mir-155', '<-', 'Lactobacillus acidophilus', '{Decreased Expression, KRAS Over Expression, Disease Decrease}', 'Colon Cancer', '10.1007/s12602-018-9478-8', '30311185'),
    ('MIG000026', 'hsa-mir-26b', '<-', 'Bifidobacterium bifidum', '{Increased Expression, APC Under Expression, PU.1 Under Expression, PTEN Under Expression, Disease Decrease}', 'Colon Cancer', '10.1007/s12602-018-9478-8', '30311185'),
    ('MIG000027', 'hsa-mir-18a', '<-', 'Bifidobacterium bifidum', '{Increased Expression, APC Under Expression, PU.1 Under Expression, PTEN Under Expression, Disease Decrease}', 'Colon Cancer', '10.1007/s12602-018-9478-8', '30311185'),
    ('MIG000028', 'hsa-mir-145', '<-', 'Bifidobacterium longum', '{Increased Expression, Disease Decrease}', 'Colorectal Cancer', '10.1080/01635581.2019.1577984', '30862187'),
    ('MIG000029', 'hsa-mir-15a', '<-', 'Bifidobacterium longum', '{Increased Expression, Disease Decrease}', 'Colorectal Cancer', '10.1080/01635581.2019.1577984', '30862187'),
    ('MIG000030', 'hsa-mir-146a', '<-', 'Bifidobacterium longum', '{Decreased Expression, Disease Decrease}', 'Colorectal Cancer', '10.1080/01635581.2019.1577984', '30862187'),
    ('MIG000031', 'hsa-mir-199a', '->', 'uncultured segmented filamentous bacterium', '{Decreased Proliferaton, Disease Decrease}', 'Inflammatory Bowel Disease', '10.1016/j.bbrc.2018.06.174', '29969632'),
    ('MIG000032', 'hsa-mir-548ab', '->', 'Fusobacterium nucleatum', '{Decreased Proliferaton, Disease Decrease}', 'Inflammatory Bowel Disease', '10.1016/j.bbrc.2018.06.174', '29969632'),
    ('MIG000033', 'hsa-mir-548ab', '->', 'Escherichia coli', '{Decreased Proliferaton, Disease Decrease}', 'Inflammatory Bowel Disease', '10.1016/j.bbrc.2018.06.174', '29969632');