INSERT INTO tabs (tab_id,name, display_name) VALUES (1,'Vitamin_A','Vitamin A');
INSERT INTO tabs (tab_id,name, display_name) VALUES (2,'Vitamin_B','Vitamin B');
INSERT INTO tabs (tab_id,name, display_name) VALUES (3,'Vitamin_C','Vitamin C');
INSERT INTO tabs (tab_id,name, display_name) VALUES (4,'Vitamin_D','Vitamin D');

INSERT INTO tab_childs (tab_child_id,name, display_name) VALUES (1,'Zones','Zones');
INSERT INTO tab_childs (tab_child_id,name, display_name) VALUES (2,'Sunshine_Availability','Sunshine Availability');

INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (1,1);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (1,2);