CREATE OR REPLACE FUNCTION insert_profile() RETURNS 
	TRIGGER AS $new_profile$
	BEGIN
		INSERT INTO profile(student_id) VALUES (NEW.id);
		RETURN NULL;
	END;
$new_profile$ LANGUAGE plpgsql;

CREATE TRIGGER new_profile AFTER INSERT ON student
	FOR EACH ROW EXECUTE PROCEDURE insert_profile();