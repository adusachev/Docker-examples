
create table customer(
	id serial primary key,
	name varchar(255),
	phone varchar(30),
	email varchar(255)
);

create table product(
	id serial primary key,
	name varchar(255),
	description text,
	price integer
);

create table product_photo(
	id serial primary key,
	url varchar(255),
	product_id integer references product(id)
);

create table cart(
	customer_id integer references customer(id),
	id serial primary key
);

create table cart_product(
	cart_id integer references cart(id),
	product_id integer references product(id)
);


insert into customer(name, phone, email) values ('Nick', '02', 'nikk@gmaill.com');
insert into customer(name, phone, email) values ('Peter', '03', 'pet@gmaill.com');

insert into product(name, description, price) values ('iPhone', 'mobile phone', 100000);
insert into product(name, description, price) values ('rolex', 'watch', 50000);

insert into product_photo(url, product_id) values ('iphone_photo', 1);

