------ Mini Project: Simple Banking System with Trigger-Based Logging  ------

----create main table
create table icici_bank(
id int primary key identity(1,1),
Name varchar(25),
Balance decimal(10,2)
);

insert into icici_bank(Name,Balance)
values('Ajay', 25000),('Baban',30000),('chaman',34000),('Dev',18000);

select * from icici_bank

----------create log table -----------
create table icici_log(
id int primary key identity(1,1),
user_id int,
Name varchar(25),
old_Balance decimal(10,2),
new_Balance decimal(10,2),
Action_type varchar(10),
log_time datetime default getdate()
);

------------ Insert Trigger ------------------
create trigger insert_trig on icici_bank after insert
as 
begin
insert into icici_log(user_id,Name,Action_type,new_Balance)
select id,name,'Insert',balance from inserted;
end;

------- Update Trigger ------------------
create trigger update_trig on icici_bank after update
as
begin
insert into icici_log(user_id,Name,Action_type,old_Balance,new_Balance)
select d.id,d.name,'Update',d.Balance,i.balance from deleted d
join inserted i 
on d.id=i.id;
end;

----------- Delete Trigger ------------------
create trigger delete_trig on icici_bank after delete
as
begin
insert into icici_log(user_id,Name,Action_type,old_Balance)
select id,name,'Delete',balance from deleted;
end;



-----------insert customers------------------
insert into icici_bank(Name,Balance)
values('Emanual',27000),('Farukh',3000);

-----------update customers-------------------
update icici_bank set Balance=Balance+20000 where name='Ajay';


-----------delete customers-------------------
delete from icici_bank where name='Farukh';


----------view log--------------------------
select * from icici_log