--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-11-10 14:10:36

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

DROP DATABASE simoti;
--
-- TOC entry 3407 (class 1262 OID 16876)
-- Name: simoti; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE simoti WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


ALTER DATABASE simoti OWNER TO postgres;

\connect simoti

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
-- TOC entry 227 (class 1255 OID 25114)
-- Name: ejemplo(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.ejemplo() RETURNS integer
    LANGUAGE plpgsql
    AS $$
BEGIN
 RETURN 104;
END;
$$;


ALTER FUNCTION public.ejemplo() OWNER TO postgres;

--
-- TOC entry 228 (class 1255 OID 25117)
-- Name: sp_verifyidentity(character varying, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.sp_verifyidentity(pusername character varying, ppassword character varying) RETURNS TABLE(id character varying, username character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
	return query
 SELECT users.id, users.username
	FROM users
    WHERE 
    users.username = pUsername 
	AND users.password = pPassword;
END;
$$;


ALTER FUNCTION public.sp_verifyidentity(pusername character varying, ppassword character varying) OWNER TO postgres;

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
-- TOC entry 3400 (class 0 OID 25105)
-- Dependencies: 225
-- Data for Name: fall_detector; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.fall_detector (id, patient_id, description, active, created_at) VALUES (1, 2, 'CAIDA FUERTE', true, '2023-11-09 17:32:03-06');
INSERT INTO public.fall_detector (id, patient_id, description, active, created_at) VALUES (2, 2, 'CAIDA FUERTE', true, '2023-11-09 17:34:39-06');
INSERT INTO public.fall_detector (id, patient_id, description, active, created_at) VALUES (3, 3, 'CAIDA FUERTE', true, '2023-11-09 17:34:42-06');
INSERT INTO public.fall_detector (id, patient_id, description, active, created_at) VALUES (4, 3, 'CAIDA FUERTE', true, '2023-11-09 17:34:43-06');
INSERT INTO public.fall_detector (id, patient_id, description, active, created_at) VALUES (5, 4, 'CAIDA FUERTE', true, '2023-11-09 17:34:46-06');
INSERT INTO public.fall_detector (id, patient_id, description, active, created_at) VALUES (6, 4, 'CAIDA LEVE', true, '2023-11-09 17:34:51-06');


--
-- TOC entry 3395 (class 0 OID 25085)
-- Dependencies: 220
-- Data for Name: heart_rate; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.heart_rate (id, patient_id, value, active, created_at) VALUES (5, 2, '110', true, '2023-11-09 15:59:27-06');


--
-- TOC entry 3394 (class 0 OID 25076)
-- Dependencies: 219
-- Data for Name: oxygen_saturation; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.oxygen_saturation (id, patient_id, value, active, created_at) VALUES (1, 1, '98', true, '2023-11-09 13:56:06-06');
INSERT INTO public.oxygen_saturation (id, patient_id, value, active, created_at) VALUES (2, 1, '99', true, '2023-11-09 12:56:25-06');
INSERT INTO public.oxygen_saturation (id, patient_id, value, active, created_at) VALUES (6, 2, '97', true, '2023-11-09 15:05:35-06');
INSERT INTO public.oxygen_saturation (id, patient_id, value, active, created_at) VALUES (7, 2, '97', true, '2023-11-09 15:05:38-06');
INSERT INTO public.oxygen_saturation (id, patient_id, value, active, created_at) VALUES (8, 2, '97', true, '2023-11-09 15:47:02-06');


--
-- TOC entry 3389 (class 0 OID 16952)
-- Dependencies: 214
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('0cf5dc68-fdee-4be2-b26e-278ac8a3d18d', 'DELETE.USER', 'Permiso para eliminar usuarios', true, '2023-08-08 17:46:42.259219', 1, '2023-08-08 17:46:42.259219', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('fd2ce686-bd12-4695-a01c-b7ce8fe02a28', 'READ.HOME', 'Permiso para botón de inicio', true, '2023-11-10 12:36:53.382103', 1, '2023-11-10 12:36:53.382103', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('c23a315f-ffe5-4c21-a885-ac9f78502d58', 'READ.MANAGEMENT', 'Permiso para ver la administración del sistema', true, '2023-11-10 13:26:23.708788', 1, '2023-11-10 13:26:23.708788', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('42da8d7a-5a4d-40a9-aad2-97d5cc8de403', 'READ.USER', 'Permiso para visualizar usuarios', true, '2023-11-10 13:26:43.162785', 1, '2023-11-10 13:26:43.162785', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('51795a02-f6b3-44bf-9d2d-a487dc8e8b0d', 'READ.ROLE', 'Permisos para listado de roles', true, '2023-11-10 13:27:35.067789', 1, '2023-11-10 13:27:35.067789', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('b40c472d-ea5b-4bcb-9b42-534048a6d2e0', 'READ.PERMISSION', 'Permiso para visualizar permisos', true, '2023-11-10 13:27:52.837213', 1, '2023-11-10 13:27:52.837213', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('4a34554d-d76b-44a0-9899-9897e82c454e', 'CREATE.ROLE', 'Permiso para crear roles', true, '2023-11-10 13:33:28.465877', 1, '2023-11-10 13:33:28.465877', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('ede1397a-eb7c-4e63-85a8-5326a78cd76f', 'EDIT.ROLE', 'Permiso para editar roles', true, '2023-11-10 13:35:16.666326', 1, '2023-11-10 13:35:16.666326', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('37caff30-1778-4834-a47d-f93da79a52ab', 'DELETE.ROLE', 'Permiso para eliminar roles', true, '2023-11-10 13:35:49.258852', 1, '2023-11-10 13:35:49.258852', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('b3e7ef26-6ce3-408c-8ec2-a1498234703a', 'CREATE.PERMISSION', 'Permiso para crear permisos', true, '2023-11-10 13:38:06.844245', 1, '2023-11-10 13:38:06.844245', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('bac67a33-6fd1-4936-aa3e-81a0252b9532', 'EDIT.PERMISSION', 'Permiso para editar permisos', true, '2023-11-10 13:38:50.211947', 1, '2023-11-10 13:38:50.211947', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('7be5ab42-eded-4f03-9e99-8ee94e62a7c7', 'DELETE.PERMISSION', 'Permisos para eliminar permisos', true, '2023-11-10 13:39:10.209817', 1, '2023-11-10 13:39:10.209817', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('ad16ad28-51d9-40b1-9963-f474f4a450fb', 'CREATE.USER', 'Permiso para crear usuarios', true, '2023-08-08 17:37:19.021716', 1, '2023-08-08 17:37:19.021716', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('cca0b84d-f50d-4b40-a70e-881ccd796eed', 'EDIT.USER', 'Permiso para editar usuarios', true, '2023-11-10 13:41:48.200141', 1, '2023-11-10 13:41:48.200141', 1);
INSERT INTO public.permissions (id, permission, description, active, created_at, created_by, updated_at, updated_by) VALUES ('a4acad21-bf2c-4e10-af14-31dc6cc61099', 'DELETE.USER', 'Permiso para eliminar usuarios', true, '2023-11-10 13:42:09.864747', 1, '2023-11-10 13:42:09.864747', 1);


--
-- TOC entry 3392 (class 0 OID 17010)
-- Dependencies: 217
-- Data for Name: role_has_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('f9ffcd6d-d463-4178-a822-6ebca5cced44', 'ad16ad28-51d9-40b1-9963-f474f4a450fb');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('f9ffcd6d-d463-4178-a822-6ebca5cced44', '0cf5dc68-fdee-4be2-b26e-278ac8a3d18d');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'b3e7ef26-6ce3-408c-8ec2-a1498234703a');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', '4a34554d-d76b-44a0-9899-9897e82c454e');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('b4463b9f-19c7-4a9c-844e-c479b0b514c0', 'ad16ad28-51d9-40b1-9963-f474f4a450fb');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('b4463b9f-19c7-4a9c-844e-c479b0b514c0', '0cf5dc68-fdee-4be2-b26e-278ac8a3d18d');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'ad16ad28-51d9-40b1-9963-f474f4a450fb');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', '7be5ab42-eded-4f03-9e99-8ee94e62a7c7');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', '37caff30-1778-4834-a47d-f93da79a52ab');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', '0cf5dc68-fdee-4be2-b26e-278ac8a3d18d');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'a4acad21-bf2c-4e10-af14-31dc6cc61099');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'bac67a33-6fd1-4936-aa3e-81a0252b9532');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'ede1397a-eb7c-4e63-85a8-5326a78cd76f');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'cca0b84d-f50d-4b40-a70e-881ccd796eed');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'fd2ce686-bd12-4695-a01c-b7ce8fe02a28');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'c23a315f-ffe5-4c21-a885-ac9f78502d58');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', 'b40c472d-ea5b-4bcb-9b42-534048a6d2e0');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', '51795a02-f6b3-44bf-9d2d-a487dc8e8b0d');
INSERT INTO public.role_has_permissions (role_id, permission_id) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', '42da8d7a-5a4d-40a9-aad2-97d5cc8de403');


--
-- TOC entry 3391 (class 0 OID 17000)
-- Dependencies: 216
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.roles (id, active, role, created_at, created_by, updated_at, updated_by) VALUES ('5b1f90fd-2e32-428a-aba0-8cf0157f5bdf', false, 'Consulta', '2023-08-17 14:22:51', 'ADMIN', '2023-11-08 18:24:41', 'ADMIN');
INSERT INTO public.roles (id, active, role, created_at, created_by, updated_at, updated_by) VALUES ('b4463b9f-19c7-4a9c-844e-c479b0b514c0', true, 'dev', '2023-11-09 13:01:39', 'ADMIN', '2023-11-09 13:01:39', 'ADMIN');
INSERT INTO public.roles (id, active, role, created_at, created_by, updated_at, updated_by) VALUES ('f9ffcd6d-d463-4178-a822-6ebca5cced44', false, 'Ad', '2023-08-17 11:22:40', 'ADMIN', '2023-08-17 11:22:40', 'ADMIN');
INSERT INTO public.roles (id, active, role, created_at, created_by, updated_at, updated_by) VALUES ('42a5f531-8616-400e-a0a9-f5660fa079d2', true, 'Administrador', '2023-11-10 12:38:05', 'ADMIN', '2023-11-10 13:42:21', 'ADMIN');


--
-- TOC entry 3396 (class 0 OID 25092)
-- Dependencies: 221
-- Data for Name: temperature; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.temperature (id, patient_id, value, active, created_at) VALUES (1, 1, '38.5', true, '2023-11-09 17:07:03-06');
INSERT INTO public.temperature (id, patient_id, value, active, created_at) VALUES (2, 1, '38.6', true, '2023-11-09 17:07:13-06');
INSERT INTO public.temperature (id, patient_id, value, active, created_at) VALUES (3, 3, '38.6', true, '2023-11-09 17:07:15-06');
INSERT INTO public.temperature (id, patient_id, value, active, created_at) VALUES (4, 2, '38', true, '2023-11-09 17:07:20-06');
INSERT INTO public.temperature (id, patient_id, value, active, created_at) VALUES (5, 5, '39', true, '2023-11-09 17:07:25-06');


--
-- TOC entry 3393 (class 0 OID 17045)
-- Dependencies: 218
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, active, created_at, created_by, last_name, middle_name, first_name, password, role_id, updated_at, updated_by, username, profile_pic_url) VALUES ('2528ccc3-1e7b-4236-8af3-c1aacaae77ff', false, '2023-10-04 10:30:54.628993', '1', 'Nuevo', 'Usuario', 'Agregar', '123456', '5b1f90fd-2e32-428a-aba0-8cf0157f5bdf', '2023-10-04 10:30:54.628993', '1', 'nuevo', NULL);
INSERT INTO public.users (id, active, created_at, created_by, last_name, middle_name, first_name, password, role_id, updated_at, updated_by, username, profile_pic_url) VALUES ('2f437232-5145-433e-a386-33019e2eb69b', false, '2023-10-04 10:35:50.684255', '1', 'admin', 'admin', 'admin', '123456', 'f9ffcd6d-d463-4178-a822-6ebca5cced44', '2023-10-04 10:35:50.684255', '1', 'admin', NULL);
INSERT INTO public.users (id, active, created_at, created_by, last_name, middle_name, first_name, password, role_id, updated_at, updated_by, username, profile_pic_url) VALUES ('f1515fd1-3f93-4303-8da4-de72801cf378', false, '2023-10-04 11:45:53.961194', '1', 'Nuevo', 'nuevo', 'nuevo', 'nuevonuevo', '5b1f90fd-2e32-428a-aba0-8cf0157f5bdf', '2023-10-04 11:45:53.961194', '1', 'nuevonuevo', NULL);
INSERT INTO public.users (id, active, created_at, created_by, last_name, middle_name, first_name, password, role_id, updated_at, updated_by, username, profile_pic_url) VALUES ('cf4aca64-aea4-4cbe-9feb-a4cebfc0a9b3', false, '2023-11-09 12:57:19.376577', '1', 'Martinez', 'Solis', 'Andrea', 'andrea', '5b1f90fd-2e32-428a-aba0-8cf0157f5bdf', '2023-11-09 12:57:19.376577', '1', 'consulta', NULL);
INSERT INTO public.users (id, active, created_at, created_by, last_name, middle_name, first_name, password, role_id, updated_at, updated_by, username, profile_pic_url) VALUES ('5b1f90fd-2e32-428a-aba0-8cf0157343bdf', true, '2023-10-04 00:00:00', '1', 'Martinez', 'Solis', 'Andrea Naraly', 'sacmex', '42a5f531-8616-400e-a0a9-f5660fa079d2', '2023-10-04 00:00:00', '1', 'naraly.solis', NULL);


--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 226
-- Name: fall_detector_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fall_detector_seq', 6, true);


--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 223
-- Name: heart_rate_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.heart_rate_seq', 5, true);


--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 222
-- Name: oxygen_saturation_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oxygen_saturation_seq', 8, true);


--
-- TOC entry 3411 (class 0 OID 0)
-- Dependencies: 215
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq', 1, false);


--
-- TOC entry 3412 (class 0 OID 0)
-- Dependencies: 224
-- Name: temperature_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temperature_seq', 5, true);


--
-- TOC entry 3237 (class 2606 OID 17016)
-- Name: role_has_permissions PK_9271906febebfc15e39b49fa738; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_has_permissions
    ADD CONSTRAINT "PK_9271906febebfc15e39b49fa738" PRIMARY KEY (role_id, permission_id);


--
-- TOC entry 3239 (class 2606 OID 17054)
-- Name: users PK_a3ffb1c0c8416b9fc6f907b7433; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "PK_a3ffb1c0c8416b9fc6f907b7433" PRIMARY KEY (id);


--
-- TOC entry 3233 (class 2606 OID 17009)
-- Name: roles PK_c1433d71a4838793a49dcad46ab; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT "PK_c1433d71a4838793a49dcad46ab" PRIMARY KEY (id);


--
-- TOC entry 3235 (class 2606 OID 17007)
-- Name: roles UQ_ccc7c1489f3a6b3c9b47d4537c5; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT "UQ_ccc7c1489f3a6b3c9b47d4537c5" UNIQUE (role);


--
-- TOC entry 3241 (class 2606 OID 17052)
-- Name: users UQ_fe0bb3f6520ee0469504521e710; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "UQ_fe0bb3f6520ee0469504521e710" UNIQUE (username);


--
-- TOC entry 3243 (class 2606 OID 25084)
-- Name: oxygen_saturation oxygen_saturation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oxygen_saturation
    ADD CONSTRAINT oxygen_saturation_pkey PRIMARY KEY (id);


--
-- TOC entry 3231 (class 2606 OID 17028)
-- Name: permissions permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3246 (class 2606 OID 17055)
-- Name: users FK_a2cecd1a3531c0b041e29ba46e1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "FK_a2cecd1a3531c0b041e29ba46e1" FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- TOC entry 3244 (class 2606 OID 25066)
-- Name: role_has_permissions fk_role_has_permissions_permissions; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_has_permissions
    ADD CONSTRAINT fk_role_has_permissions_permissions FOREIGN KEY (permission_id) REFERENCES public.permissions(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 3245 (class 2606 OID 25071)
-- Name: role_has_permissions fk_role_has_permissions_roles; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role_has_permissions
    ADD CONSTRAINT fk_role_has_permissions_roles FOREIGN KEY (role_id) REFERENCES public.roles(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


-- Completed on 2023-11-10 14:10:36

--
-- PostgreSQL database dump complete
--

