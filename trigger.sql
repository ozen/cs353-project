CREATE TRIGGER "occupid_seats_increment" AFTER INSERT ON "Ticket" 
BEGIN
update Voyage set occupied_seats = occupied_seats+1 where id=new.voyage_id;
END