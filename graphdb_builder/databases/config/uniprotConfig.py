###### UniProt Database ########
uniprot_ftp = "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/"
uniprot_id_url = uniprot_ftp+"idmapping/by_organism/HUMAN_9606_idmapping.dat.gz"
uniprot_text_file = "../../../data/databases/UniProt/uniprot-human.tab" #### Downloaded manually from UniProt until we know url (organism:human AND reviewed:yes)
uniprot_variant_file = uniprot_ftp+"variants/homo_sapiens_variation.txt.gz"
uniprot_peptides_files = [uniprot_ftp+"proteomics_mapping/UP000005640_9606_nonUniquePeptides.tsv",
                            uniprot_ftp+"proteomics_mapping/UP000005640_9606_uniquePeptides.tsv"]
uniprot_go_annotations = "http://geneontology.org/gene-associations/goa_human.gaf.gz"
uniprot_ids = ["UniProtKB-ID", 
                "NCBI_TaxID", 
                "Gene_Name", 
                "RefSeq", 
                "PDB", 
                "STRING", 
                "KEGG", 
                "Reactome", 
                "HPA", 
                "ChEMBL", 
                "Ensembl"]
uniprot_synonyms = ["UniProtKB-ID", 
                    "Gene_Name", 
                    "STRING", 
                    "HPA", 
                    "Ensembl", 
                    "ChEMBL", 
                    "PDB"]
uniprot_protein_relationships = {"RefSeq": ("Transcript", "TRANSLATED_INTO"), 
                                "Gene_Name":("Gene","TRANSLATED_INTO")
                                }
proteins_header = ['ID', ':LABEL', 'accession','name', 'synonyms', 'description', 'taxid']
variants_header = ['ID', ':LABEL', 'alternative_names']
peptides_header = ['ID', ':LABEL', 'type', 'unique']
relationships_header = ['START_ID', 'END_ID','TYPE', 'source']
go_header = ['START_ID', 'END_ID', 'TYPE', 'evidence_type','score','source']