##STEP1 ADD BELOW CODE TO COMMAND LINE

DROP TABLE IF EXISTS microrna_disease;
CREATE TABLE microrna_disease
(
  miRBase_ID  VARCHAR(25),
  Disease_Name VARCHAR(200)
);

##STEP2 ADD VALUES TO COMMAND LINE FROM TEXT FILE using the COPY command

##STEP3 

ALTER TABLE microrna_disease
	ADD COLUMN id SERIAL PRIMARY KEY;