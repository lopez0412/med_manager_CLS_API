DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addPaciente`(IN `p_nombre` VARCHAR(70), IN `p_numeroRegistro` VARCHAR(20), IN `p_genId` INT, IN `p_edad` VARCHAR(10), IN `p_direccion` VARCHAR(200), IN `p_depId` INT, IN `p_munId` INT, IN `p_estadoCivil` INT, IN `p_telefono` VARCHAR(12), IN `p_fechaNacimiento` VARCHAR(20), IN `p_numeroDui` VARCHAR(12), IN `p_nombreMadre` VARCHAR(100), IN `p_nombrePadre` VARCHAR(100), IN `p_responsable` VARCHAR(100), IN `p_telContacto` VARCHAR(12), IN `p_idUsuarioCrea` INT)
BEGIN
    -- Verificar y asignar valores nulos si es necesario
    DECLARE numero_dui VARCHAR(12);
    DECLARE nombre_madre VARCHAR(100);
    DECLARE nombre_padre VARCHAR(100);
    DECLARE responsable_v VARCHAR(100);
    DECLARE tel_contacto VARCHAR(12);
 

    IF p_numeroDui IS NULL THEN
        SET numero_dui = NULL;
    ELSE
        SET numero_dui = p_numeroDui;
    END IF;

    IF p_nombreMadre IS NULL THEN
        SET nombre_madre = NULL;
    ELSE
        SET nombre_madre = p_nombreMadre;
    END IF;
    
    IF p_nombrePadre IS NULL THEN
        SET nombre_padre = NULL;
    ELSE
        SET nombre_padre = p_nombrePadre;
    END IF;
    
    IF p_responsable IS NULL THEN
        SET responsable_v = NULL;
    ELSE
        SET responsable_v = p_responsable;
    END IF;
    
    IF p_telContacto IS NULL THEN
        SET tel_contacto = NULL;
    ELSE
        SET tel_contacto = p_telContacto;
    END IF;

    -- Inserción de datos en la tabla
    -- Inserción de datos en la tabla
    INSERT INTO pacientes (
        nombre, 
        numeroRegistro, 
        genId, 
        edad, 
        direccion, 
        depId, 
        munId, 
        estadoCivil, 
        telefono, 
        fechaNacimiento, 
        numeroDui, 
        nombreMadre, 
        nombrePadre, 
        responsable, 
        telContacto, 
        idUsuarioCreacion, 
        fechaCreacion
    ) 
    VALUES (
        p_nombre, 
        p_numeroRegistro, 
        p_genId, 
        p_edad, 
        p_direccion, 
        p_depId, 
        p_munId, 
        p_estadoCivil, 
        p_telefono, 
        p_fechaNacimiento, 
        numero_dui, 
        nombre_madre, 
        nombre_padre, 
        responsable_v, 
        tel_contacto, 
        p_idUsuarioCrea, 
        NOW()
    );
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addUser`(IN pUsername VARCHAR(20), IN pPassword VARCHAR(20), IN pFullname VARCHAR(50), IN p_email VARCHAR(20))
BEGIN
    INSERT INTO user (username, password, fullname, email)
    VALUES (pUsername, AES_ENCRYPT(pPassword, SHA2('BWvc351?C2KHNL3125D', 512)), pFullname, pEmail);
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_borrarPaciente`(
    IN p_idPaciente INT
)
BEGIN
    DELETE FROM pacientes
    WHERE pacienteId = p_idPaciente;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscarPaciente`(IN `p_busqueda` VARCHAR(30))
BEGIN
    SET @sql = CONCAT("SELECT * FROM pacientes WHERE nombre LIKE '%", p_busqueda, "%' OR telefono LIKE '%", p_busqueda, "%' OR numeroDui LIKE '%", p_busqueda, "%' OR direccion LIKE '%", p_busqueda, "%'");
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_listPacientes`()
BEGIN
	SELECT *
    FROM pacientes 
    ORDER BY pacienteId DESC
    LIMIT 200;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_verifyIdentity`(IN pUsername VARCHAR(20), IN pPassword VARCHAR(20))
BEGIN
	SELECT USER.id, USER.username, USER.fullname, USER.email 
	FROM user USER 
    WHERE 1 = 1 
    AND USER.username = pUsername 
	AND CAST(AES_DECRYPT(USER.password, SHA2('BWvc351?C2KHNL3125D', 512)) AS CHAR(30)) = pPassword;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_editarPaciente`(IN `p_idPaciente` INT, IN `p_nombre` VARCHAR(70), IN `p_numeroRegistro` VARCHAR(20), IN `p_genId` INT, IN `p_edad` VARCHAR(10), IN `p_direccion` VARCHAR(200), IN `p_depId` INT, IN `p_munId` INT, IN `p_estadoCivil` INT, IN `p_telefono` VARCHAR(12), IN `p_fechaNacimiento` VARCHAR(20), IN `p_numeroDui` VARCHAR(12), IN `p_nombreMadre` VARCHAR(100), IN `p_nombrePadre` VARCHAR(100), IN `p_responsable` VARCHAR(100), IN `p_telContacto` VARCHAR(12), IN `p_idUsuarioModifica` INT)
BEGIN
    UPDATE pacientes
    SET
        nombre = p_nombre,
        numeroRegistro = p_numeroRegistro,
        genId = p_genId,
        edad = p_edad,
        direccion = p_direccion,
        depId = p_depId,
        munId = p_munId,
        estadoCivil = p_estadoCivil,
        telefono = p_telefono,
        fechaNacimiento = p_fechaNacimiento,
        numeroDui = p_numeroDui,
        nombreMadre = p_nombreMadre,
        nombrePadre = p_nombrePadre,
        responsable = p_responsable,
        telContacto = p_telContacto,
        idUsuarioModifica = p_idUsuarioModifica,
        fechaModificacion = NOW()
    WHERE pacienteId = p_idPaciente;
END$$
DELIMITER ;
