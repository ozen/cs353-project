CREATE TRIGGER "occupied_seats_increment" AFTER INSERT ON "Ticket" 
BEGIN
update Voyage set occupied_seats = occupied_seats+1 where id=new.voyage_id;
END;
CREATE TRIGGER "reserved_seats_increment" AFTER INSERT ON "Reservation" 
BEGIN
update Voyage set occupied_seats = occupied_seats+1 where id=new.voyage_id;
END;
CREATE TRIGGER "reserved_seats_decrement" AFTER DELETE ON "Reservation" 
BEGIN
update Voyage set occupied_seats = occupied_seats-1 where id=new.voyage_id;
END;
CREATE TRIGGER "occupied_seats_decrement" AFTER DELETE ON "Ticket" 
BEGIN
update Voyage set occupied_seats = occupied_seats-1 where id=new.voyage_id;
END;