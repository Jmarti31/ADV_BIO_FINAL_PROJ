DROP TABLE IF EXISTS Taxonomy;
CREATE TABLE Taxonomy
(
   organsim_name VARCHAR(110) NOT NULL,
   node_rank VARCHAR(18),
   ncbi_taxon_id INTEGER,
   taxon_id INTEGER,
   parent_taxon_id INTEGER,
   superkingdom VARCHAR(15)
);