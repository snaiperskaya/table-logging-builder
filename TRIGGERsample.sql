CREATE OR REPLACE TRIGGER {?}_BIU
before insert or update on {?}
for each row
begin
 select sysdate, logging_utl.get_user_info into :new.u_date, :new.u_name from dual;
end;
/