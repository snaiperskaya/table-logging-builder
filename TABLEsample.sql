ALTER TABLE {?}
ADD (
	U_NAME			VARCHAR2(250 CHAR)		DEFAULT 'user' 		NOT NULL,
	U_DATE			DATE					DEFAULT SYSDATE		NOT NULL
);
/

COMMENT ON COLUMN {?}.U_NAME IS 'User Name for audit logging purposes';
COMMENT ON COLUMN {?}.U_DATE IS 'Date/time for audit logging purposes';
/