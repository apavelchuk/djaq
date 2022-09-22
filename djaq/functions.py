function_whitelist = [
    "AVG",
    "COUNT",
    "MAX",
    "MIN",
    "SUM",
    "STDDEV",
    "VARIANCE",
    "TOTAL",
    "GROUP_CONCAT",
    "AREA",
    "CENTER",
    "DIAMETER",
    "HEIGHT",
    "ISCLOSED",
    "ISOPEN",
    "LENGTH",
    "NPOINTS",
    "PCLOSE",
    "POPEN",
    "RADIUS",
    "WIDTH",
    "BOX",
    "CIRCLE",
    "LSEG",
    "PATH",
    "POINT",
    "POLYGON",
    "LENGTH",
    "NUMNODE",
    "PLAINTO_TSQUERY",
    "QUERYTREE",
    "SETWEIGHT",
    "STRIP",
    "TO_TSQUERY",
    "TS_HEADLINE",
    "TS_RANK",
    "TS_RANK_CD",
    "TS_REWRITE",
    "TS_REWRITE",
    "COALESCE",
    "NULLIF",
    "GREATEST",
    "LEAST",
    "GENERATE_SERIES",
    "TO_CHAR",
    "TO_DATE",
    "TO_NUMBER",
    "TO_TIMESTAMP",
    "AGE",
    "DATE_PART",
    "DATE_TRUNC",
    "EXTRACT",
    "ISFINITE",
    "JUSTIFY_DAYS",
    "JUSTIFY_HOURS",
    "JUSTIFY_INTERVAL",
    "NOW",
    "STATEMENT_TIMESTAMP",
    "TIMEOFDAY",
    "TRANSACTION_TIMESTAMP",
    "BIT_LENGTH",
    "CHAR_LENGTH",
    "CHARACTER_LENGTH",
    "LOWER",
    "OCTET_LENGTH",
    "OVERLAY",
    "POSITION",
    "SUBSTRING",
    "TRIM",
    "UPPER",
    "ASCII",
    "BTRIM",
    "CHR",
    "CONCAT",
    "CONCAT_WS",
    "CONVERT",
    "CONVERT_FROM",
    "CONVERT_TO",
    "DECODE",
    "ENCODE",
    "FORMAT",
    "INITCAP",
    "LEFT",
    "LENGTH",
    "LENGTH",
    "LPAD",
    "LTRIM",
    "MD5",
    "PG_CLIENT_ENCODING",
    "QUOTE_IDENT",
    "QUOTE_LITERAL",
    "QUOTE_NULLABLE",
    "REGEXP_MATCHES",
    "REGEXP_REPLACE",
    "REGEXP_SPLIT_TO_ARRAY",
    "REGEXP_SPLIT_TO_TABLE",
    "REPEAT",
    "REPLACE",
    "REVERSE",
    "RIGHT",
    "RPAD",
    "RTRIM",
    "SPLIT_PART",
    "STRPOS",
    "SUBSTR",
    "TO_ASCII",
    "TO_HEX",
    "TRANSLATE",
    "ABS",
    "CEIL",
    "CEILING",
    "DEGREES",
    "DIV",
    "EXP",
    "FLOOR",
    "LN",
    "LOG",
    "MOD",
    "PI",
    "POWER",
    "RADIANS",
    "ROUND",
    "SIGN",
    "SQRT",
    "TRUNC",
    "WIDTH_BUCKET",
    "SET_SEED",
    "RANDOM",
    "ACOS",
    "ASIN",
    "ATAN",
    "ATAN2",
    "COS",
    "SIN",
    "TAN",
    "COT",
    "BOX2D",
    "BOX3D",
    "GEOMETRYTYPE",
    "POSTGIS_ADDBBOX",
    "POSTGIS_DROPBBOX",
    "POSTGIS_HASBBOX",
    "ST_3DAREA",
    "ST_3DCLOSESTPOINT",
    "ST_3DDIFFERENCE",
    "ST_3DDISTANCE",
    "ST_3DEXTENT",
    "ST_3DINTERSECTION",
    "ST_3DLENGTH",
    "ST_3DLINEINTERPOLATEPOINT",
    "ST_3DLONGESTLINE",
    "ST_3DMAKEBOX",
    "ST_3DMAXDISTANCE",
    "ST_3DPERIMETER",
    "ST_3DSHORTESTLINE",
    "ST_3DUNION",
    "ST_ADDMEASURE",
    "ST_ADDPOINT",
    "ST_AFFINE",
    "ST_ANGLE",
    "ST_APPROXIMATEMEDIALAXIS",
    "ST_AREA",
    "ST_AZIMUTH",
    "ST_BOUNDARY",
    "ST_BOUNDINGDIAGONAL",
    "ST_BUFFER",
    "ST_BUILDAREA",
    "ST_CPAWITHIN",
    "ST_CENTROID",
    "ST_CHAIKINSMOOTHING",
    "ST_CLIPBYBOX2D",
    "ST_CLOSESTPOINT",
    "ST_CLOSESTPOINTOFAPPROACH",
    "ST_CLUSTERDBSCAN",
    "ST_CLUSTERINTERSECTING",
    "ST_CLUSTERKMEANS",
    "ST_CLUSTERWITHIN",
    "ST_COLLECT",
    "ST_COLLECTIONEXTRACT",
    "ST_COLLECTIONHOMOGENIZE",
    "ST_CONCAVEHULL",
    "ST_CONSTRAINEDDELAUNAYTRIANGLES",
    "ST_CONVEXHULL",
    "ST_COORDDIM",
    "ST_CURVETOLINE",
    "ST_DELAUNAYTRIANGLES",
    "ST_DIFFERENCE",
    "ST_DIMENSION",
    "ST_DISTANCE",
    "ST_DISTANCECPA",
    "ST_DISTANCESPHERE",
    "ST_DISTANCESPHEROID",
    "ST_DUMP",
    "ST_DUMPPOINTS",
    "ST_DUMPRINGS",
    "ST_ENDPOINT",
    "ST_ENVELOPE",
    "ST_ESTIMATEDEXTENT",
    "ST_EXPAND",
    "ST_EXTENT",
    "ST_EXTERIORRING",
    "ST_EXTRUDE",
    "ST_FILTERBYM",
    "ST_FLIPCOORDINATES",
    "ST_FORCE2D",
    "ST_FORCECURVE",
    "ST_FORCELHR",
    "ST_FORCEPOLYGONCCW",
    "ST_FORCEPOLYGONCW",
    "ST_FORCERHR",
    "ST_FORCESFS",
    "ST_FORCE3D",
    "ST_FORCE3DM",
    "ST_FORCE3DZ",
    "ST_FORCE4D",
    "ST_FORCECOLLECTION",
    "ST_FRECHETDISTANCE",
    "ST_GENERATEPOINTS",
    "ST_GEOMETRICMEDIAN",
    "ST_GEOMETRYN",
    "ST_GEOMETRYTYPE",
    "ST_HASARC",
    "ST_HAUSDORFFDISTANCE",
    "ST_INTERIORRINGN",
    "ST_INTERPOLATEPOINT",
    "ST_INTERSECTION",
    "ST_ISCLOSED",
    "ST_ISCOLLECTION",
    "ST_ISEMPTY",
    "ST_ISPLANAR",
    "ST_ISPOLYGONCCW",
    "ST_ISPOLYGONCW",
    "ST_ISRING",
    "ST_ISSIMPLE",
    "ST_ISSOLID",
    "ST_ISVALID",
    "ST_ISVALIDDETAIL",
    "ST_ISVALIDREASON",
    "ST_ISVALIDTRAJECTORY",
    "ST_LENGTH",
    "ST_LENGTH2D",
    "ST_LENGTHSPHEROID",
    "ST_LINEFROMMULTIPOINT",
    "ST_LINEINTERPOLATEPOINT",
    "ST_LINEINTERPOLATEPOINTS",
    "ST_LINELOCATEPOINT",
    "ST_LINEMERGE",
    "ST_LINESUBSTRING",
    "ST_LINETOCURVE",
    "ST_LOCATEALONG",
    "ST_LOCATEBETWEEN",
    "ST_LOCATEBETWEENELEVATIONS",
    "ST_LONGESTLINE",
    "ST_M",
    "ST_MAKEBOX2D",
    "ST_MAKEENVELOPE",
    "ST_MAKELINE",
    "ST_MAKEPOINT",
    "ST_MAKEPOINTM",
    "ST_MAKEPOLYGON",
    "ST_MAKESOLID",
    "ST_MAKEVALID",
    "ST_MAXDISTANCE",
    "ST_MEMSIZE",
    "ST_MEMUNION",
    "ST_MINIMUMBOUNDINGCIRCLE",
    "ST_MINIMUMBOUNDINGRADIUS",
    "ST_MINIMUMCLEARANCE",
    "ST_MINIMUMCLEARANCELINE",
    "ST_MINKOWSKISUM",
    "ST_MULTI",
    "ST_NDIMS",
    "ST_NPOINTS",
    "ST_NRINGS",
    "ST_NODE",
    "ST_NORMALIZE",
    "ST_NUMGEOMETRIES",
    "ST_NUMINTERIORRING",
    "ST_NUMINTERIORRINGS",
    "ST_NUMPATCHES",
    "ST_NUMPOINTS",
    "ST_OFFSETCURVE",
    "ST_ORIENTATION",
    "ST_ORIENTEDENVELOPE",
    "ST_PATCHN",
    "ST_PERIMETER",
    "ST_PERIMETER2D",
    "ST_POINT",
    "ST_POINTN",
    "ST_POINTONSURFACE",
    "ST_POINTS",
    "ST_POLYGON",
    "ST_POLYGONIZE",
    "ST_PROJECT",
    "ST_QUANTIZECOORDINATES",
    "ST_REMOVEPOINT",
    "ST_REMOVEREPEATEDPOINTS",
    "ST_REVERSE",
    "ST_ROTATE",
    "ST_ROTATEX",
    "ST_ROTATEY",
    "ST_ROTATEZ",
    "ST_SRID",
    "ST_SCALE",
    "ST_SEGMENTIZE",
    "ST_SETEFFECTIVEAREA",
    "ST_SETPOINT",
    "ST_SETSRID",
    "ST_SHAREDPATHS",
    "ST_SHIFTLONGITUDE",
    "ST_SHORTESTLINE",
    "ST_SIMPLIFY",
    "ST_SIMPLIFYPRESERVETOPOLOGY",
    "ST_SIMPLIFYVW",
    "ST_SNAP",
    "ST_SNAPTOGRID",
    "ST_SPLIT",
    "ST_STARTPOINT",
    "ST_STRAIGHTSKELETON",
    "ST_SUBDIVIDE",
    "ST_SUMMARY",
    "ST_SWAPORDINATES",
    "ST_SYMDIFFERENCE",
    "ST_TESSELATE",
    "ST_TILEENVELOPE",
    "ST_TRANSSCALE",
    "ST_TRANSFORM",
    "ST_TRANSLATE",
    "ST_UNARYUNION",
    "ST_UNION",
    "ST_VOLUME",
    "ST_VORONOILINES",
    "ST_VORONOIPOLYGONS",
    "ST_WRAPX",
    "ST_X",
    "ST_XMAX",
    "ST_XMIN",
    "ST_Y",
    "ST_YMAX",
    "ST_YMIN",
    "ST_Z",
    "ST_ZMAX",
    "ST_ZMIN",
    "ST_ZMFLAG",
]
