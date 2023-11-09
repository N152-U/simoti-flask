--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-11-09 17:41:02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 226 (class 1259 OID 25112)
-- Name: fall_detector_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fall_detector_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fall_detector_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 225 (class 1259 OID 25105)
-- Name: fall_detector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fall_detector (
    id integer DEFAULT nextval('public.fall_detector_seq'::regclass) NOT NULL,
    patient_id integer,
    description character varying,
    active boolean DEFAULT true,
    created_at timestamp with time zone DEFAULT (now())::timestamp(0) without time zone
);


ALTER TABLE public.fall_detector OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 25101)
-- Name: heart_rate_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.heart_rate_seq
    START WITH 5
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.heart_rate_seq OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 25085)
-- Name: heart_rate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.heart_rate (
    id integer DEFAULT nextval('public.heart_rate_seq'::regclass) NOT NULL,
    patient_id integer,
    value character varying,
    active boolean DEFAULT true,
    created_at timestamp with time zone DEFAULT (now())::timestamp(0) without time zone
);


ALTER TABLE public.heart_rate OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 25099)
-- Name: oxygen_saturation_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oxygen_saturation_seq
    START WITH 5
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oxygen_saturation_seq OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 25076)
-- Name: oxygen_saturation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oxygen_saturation (
    id integer DEFAULT nextval('public.oxygen_saturation_seq'::regclass) NOT NULL,
    patient_id integer,
    value character varying,
    active boolean DEFAULT true,
    created_at timestamp with time zone DEFAULT (now())::timestamp(0) without time zone
);


ALTER TABLE public.oxygen_saturation OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16952)
-- Name: permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permissions (
    id character varying NOT NULL,
    permission character varying NOT NULL,
    description character varying NOT NULL,
    active boolean DEFAULT true NOT NULL,
    created_at timestamp(6) without time zone DEFAULT now() NOT NULL,
    created_by integer DEFAULT 1 NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT now() NOT NULL,
    updated_by integer DEFAULT 1 NOT NULL
);


ALTER TABLE public.permissions OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 17010)
-- Name: role_has_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.role_has_permissions (
    role_id character varying NOT NULL,
    permission_id character varying NOT NULL
);


ALTER TABLE public.role_has_permissions OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17000)
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id character varying NOT NULL,
    active boolean DEFAULT true NOT NULL,
    role character varying NOT NULL,
    created_at timestamp(6) without time zone NOT NULL,
    created_by character varying NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL,
    updated_by character varying NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16966)
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_id_seq OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 25103)
-- Name: temperature_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.temperature_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.temperature_seq OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 25092)
-- Name: temperature; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temperature (
    id integer DEFAULT nextval('public.temperature_seq'::regclass) NOT NULL,
    patient_id integer,
    value character varying,
    active boolean DEFAULT true,
    created_at timestamp with time zone DEFAULT (now())::timestamp(0) without time zone
);


ALTER TABLE public.temperature OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 17045)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying NOT NULL,
    active boolean DEFAULT true NOT NULL,
    created_at timestamp(6) without time zone DEFAULT now() NOT NULL,
    created_by character varying DEFAULT 1 NOT NULL,
    last_name character varying NOT NULL,
    middle_name character varying NOT NULL,
    first_name character varying NOT NULL,
    password character varying NOT NULL,
    role_id character varying NOT NULL,
    updated_at timestamp(6) without time zone DEFAULT now() NOT NULL,
    updated_by character varying DEFAULT 1 NOT NULL,
    username character varying NOT NULL,
    profile_pic_url character varying
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3398 (class 0 OID 25105)
-- Dependencies: 225
-- Data for Name: fall_detector; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fall_detector (id, patient_id, description, active, created_at) FROM stdin;
1	2	CAIDA FUERTE	t	2023-11-09 17:32:03-06
2	2	CAIDA FUERTE	t	2023-11-09 17:34:39-06
3	3	CAIDA FUERTE	t	2023-11-09 17:34:42-06
4	3	CAIDA FUERTE	t	2023-11-09 17:34:43-06
5	4	CAIDA FUERTE	t	2023-11-09 17:34:46-06
6	4	CAIDA LEVE	t	2023-11-09 17:34:51-06
\.


--
-- TOC entry 3393 (class 0 OID 25085)
-- Dependencies: 220
-- Data for Name: heart_rate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.heart_rate (id, patient_id, value, active, created_at) FROM stdin;
5	2	110	t	2023-11-09 15:59:27-06
\.


--
-- TOC entry 3392 (class 0 OID 25076)
-- Dependencies: 219
-- Data for Name: oxygen_saturation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oxygen_saturation (id, patient_id, value, active, created_at) FROM stdin;
1	1	98	t	2023-11-09 13:56:06-06
2	1	99	t	2023-11-09 12:56:25-06
6	2	97	t	2023-11-09 15:05:35-06
7	2	97	t	2023-11-09 15:05:38-06
8	2	97	t	2023-11-09 15:47:02-06
\.


--
-- TOC entry 3387 (class 0 OID 16952)
-- Dependencies: 214
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) FROM stdin;
0cf5dc68-fdee-4be2-b26e-278ac8a3d18d	DELETE.USER	Permiso para eliminar usuarios	t	2023-08-08 17:46:42.259219	1	2023-08-08 17:46:42.259219	1
4cbf1a69-7de5-407a-a795-f02b2824c114	NUEVO.ANGULARACT	Permiso creado angular NEW	t	2023-08-16 12:06:33.800395	1	2023-08-16 12:06:33.800395	1
ad16ad28-51d9-40b1-9963-f474f4a450fb	CREATE.USER	Permiso para crear usuarios edición	t	2023-08-08 17:37:19.021716	1	2023-08-08 17:37:19.021716	1
d4a7187c-4a62-4573-a670-e9c4585c5106	NUEVO.PERMISO	PERMISO NUEVO	t	2023-11-08 18:19:42.817446	1	2023-11-08 18:19:42.817446	1
\.


--
-- TOC entry 3390 (class 0 OID 17010)
-- Dependencies: 217
-- Data for Name: role_has_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.role_has_permissions (role_id, permission_id) FROM stdin;
f9ffcd6d-d463-4178-a822-6ebca5cced44	ad16ad28-51d9-40b1-9963-f474f4a450fb
f9ffcd6d-d463-4178-a822-6ebca5cced44	0cf5dc68-fdee-4be2-b26e-278ac8a3d18d
f9ffcd6d-d463-4178-a822-6ebca5cced44	4cbf1a69-7de5-407a-a795-f02b2824c114
5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	0cf5dc68-fdee-4be2-b26e-278ac8a3d18d
5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	4cbf1a69-7de5-407a-a795-f02b2824c114
5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	d4a7187c-4a62-4573-a670-e9c4585c5106
b4463b9f-19c7-4a9c-844e-c479b0b514c0	ad16ad28-51d9-40b1-9963-f474f4a450fb
b4463b9f-19c7-4a9c-844e-c479b0b514c0	0cf5dc68-fdee-4be2-b26e-278ac8a3d18d
b4463b9f-19c7-4a9c-844e-c479b0b514c0	4cbf1a69-7de5-407a-a795-f02b2824c114
b4463b9f-19c7-4a9c-844e-c479b0b514c0	d4a7187c-4a62-4573-a670-e9c4585c5106
\.


--
-- TOC entry 3389 (class 0 OID 17000)
-- Dependencies: 216
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id, active, role, created_at, created_by, updated_at, updated_by) FROM stdin;
f9ffcd6d-d463-4178-a822-6ebca5cced44	f	Administrador	2023-08-17 11:22:40	ADMIN	2023-08-17 11:22:40	ADMIN
5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	f	Consulta	2023-08-17 14:22:51	ADMIN	2023-11-08 18:24:41	ADMIN
b4463b9f-19c7-4a9c-844e-c479b0b514c0	t	dev	2023-11-09 13:01:39	ADMIN	2023-11-09 13:01:39	ADMIN
\.


--
-- TOC entry 3394 (class 0 OID 25092)
-- Dependencies: 221
-- Data for Name: temperature; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temperature (id, patient_id, value, active, created_at) FROM stdin;
1	1	38.5	t	2023-11-09 17:07:03-06
2	1	38.6	t	2023-11-09 17:07:13-06
3	3	38.6	t	2023-11-09 17:07:15-06
4	2	38	t	2023-11-09 17:07:20-06
5	5	39	t	2023-11-09 17:07:25-06
\.


--
-- TOC entry 3391 (class 0 OID 17045)
-- Dependencies: 218
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, active, created_at, created_by, last_name, middle_name, first_name, password, role_id, updated_at, updated_by, username, profile_pic_url) FROM stdin;
2528ccc3-1e7b-4236-8af3-c1aacaae77ff	f	2023-10-04 10:30:54.628993	1	Nuevo	Usuario	Agregar	123456	5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	2023-10-04 10:30:54.628993	1	nuevo	\N
2f437232-5145-433e-a386-33019e2eb69b	f	2023-10-04 10:35:50.684255	1	admin	admin	admin	123456	f9ffcd6d-d463-4178-a822-6ebca5cced44	2023-10-04 10:35:50.684255	1	admin	\N
f1515fd1-3f93-4303-8da4-de72801cf378	f	2023-10-04 11:45:53.961194	1	Nuevo	nuevo	nuevo	nuevonuevo	5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	2023-10-04 11:45:53.961194	1	nuevonuevo	\N
cf4aca64-aea4-4cbe-9feb-a4cebfc0a9b3	f	2023-11-09 12:57:19.376577	1	Martinez	Solis	Andrea	andrea	5b1f90fd-2e32-428a-aba0-8cf0157f5bdf	2023-11-09 12:57:19.376577	1	consulta	\N
5b1f90fd-2e32-428a-aba0-8cf0157343bdf	t	2023-10-04 00:00:00	1	Martinez	Solis	Andrea Naraly	sacmex	b4463b9f-19c7-4a9c-844e-c479b0b514c0	2023-10-04 00:00:00	1	naraly.solis	\N
\.


--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 226
-- Name: fall_detector_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fall_detector_seq', 6, true);


--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 223
-- Name: heart_rate_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.heart_rate_seq', 5, true);


--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 222
-- Name: oxygen_saturation_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oxygen_saturation_seq', 8, true);


--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 215
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq', 1, false);


--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 224
-- Name: temperature_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temperature_seq', 5, true);


--
-- TOC entry 3235 (class 2606 OID 17016)
-- Name: role_has_permissions PK_9271906febebfc15e39b49fa738; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_has_permissions
    ADD CONSTRAINT "PK_9271906febebfc15e39b49fa738" PRIMARY KEY (role_id, permission_id);


--
-- TOC entry 3237 (class 2606 OID 17054)
-- Name: users PK_a3ffb1c0c8416b9fc6f907b7433; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "PK_a3ffb1c0c8416b9fc6f907b7433" PRIMARY KEY (id);


--
-- TOC entry 3231 (class 2606 OID 17009)
-- Name: roles PK_c1433d71a4838793a49dcad46ab; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT "PK_c1433d71a4838793a49dcad46ab" PRIMARY KEY (id);


--
-- TOC entry 3233 (class 2606 OID 17007)
-- Name: roles UQ_ccc7c1489f3a6b3c9b47d4537c5; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT "UQ_ccc7c1489f3a6b3c9b47d4537c5" UNIQUE (role);


--
-- TOC entry 3239 (class 2606 OID 17052)
-- Name: users UQ_fe0bb3f6520ee0469504521e710; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "UQ_fe0bb3f6520ee0469504521e710" UNIQUE (username);


--
-- TOC entry 3241 (class 2606 OID 25084)
-- Name: oxygen_saturation oxygen_saturation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oxygen_saturation
    ADD CONSTRAINT oxygen_saturation_pkey PRIMARY KEY (id);


--
-- TOC entry 3229 (class 2606 OID 17028)
-- Name: permissions permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3244 (class 2606 OID 17055)
-- Name: users FK_a2cecd1a3531c0b041e29ba46e1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "FK_a2cecd1a3531c0b041e29ba46e1" FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- TOC entry 3242 (class 2606 OID 25066)
-- Name: role_has_permissions fk_role_has_permissions_permissions; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_has_permissions
    ADD CONSTRAINT fk_role_has_permissions_permissions FOREIGN KEY (permission_id) REFERENCES public.permissions(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 3243 (class 2606 OID 25071)
-- Name: role_has_permissions fk_role_has_permissions_roles; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_has_permissions
    ADD CONSTRAINT fk_role_has_permissions_roles FOREIGN KEY (role_id) REFERENCES public.roles(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


-- Completed on 2023-11-09 17:41:02

--
-- PostgreSQL database dump complete
--

