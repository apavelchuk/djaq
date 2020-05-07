function_whitelist = [
    "avg",
    "count",
    "max",
    "min",
    "sum",
    "stddev",
    "variance",
    "total",
    "group_concat",
    "area",
    "center",
    "diameter",
    "height",
    "isclosed",
    "isopen",
    "length",
    "npoints",
    "pclose",
    "popen",
    "radius",
    "width",
    "box",
    "circle",
    "lseg",
    "path",
    "point",
    "polygon",
    "length",
    "numnode",
    "plainto_tsquery",
    "querytree",
    "setweight",
    "strip",
    "to_tsquery",
    "ts_headline",
    "ts_rank",
    "ts_rank_cd",
    "ts_rewrite",
    "ts_rewrite",
    "coalesce",
    "nullif",
    "greatest",
    "least",
    "generate_series",
    "to_char",
    "to_date",
    "to_number",
    "to_timestamp",
    "age",
    "date_part",
    "date_trunc",
    "extract",
    "isfinite",
    "justify_days",
    "justify_hours",
    "justify_interval",
    "now",
    "statement_timestamp",
    "timeofday",
    "transaction_timestamp",
    "bit_length",
    "char_length",
    "character_length",
    "lower",
    "octet_length",
    "overlay",
    "position",
    "substring",
    "trim",
    "upper",
    "ascii",
    "btrim",
    "chr",
    "concat",
    "concat_ws",
    "convert",
    "convert_from",
    "convert_to",
    "decode",
    "encode",
    "format",
    "initcap",
    "left",
    "length",
    "length",
    "lpad",
    "ltrim",
    "md5",
    "pg_client_encoding",
    "quote_ident",
    "quote_literal",
    "quote_nullable",
    "regexp_matches",
    "regexp_replace",
    "regexp_split_to_array",
    "regexp_split_to_table",
    "repeat",
    "replace",
    "reverse",
    "right",
    "rpad",
    "rtrim",
    "split_part",
    "strpos",
    "substr",
    "to_ascii",
    "to_hex",
    "translate",
    "abs",
    "ceil",
    "ceiling",
    "degrees",
    "div",
    "exp",
    "floor",
    "ln",
    "log",
    "mod",
    "pi",
    "power",
    "radians",
    "round",
    "sign",
    "sqrt",
    "trunc",
    "width_bucket",
    "set_seed",
    "random" "acos",
    "asin",
    "atan",
    "atan2",
    "cos",
    "sin",
    "tan",
    "cot",
    "Box2D",
    "Box3D",
    "GeometryType",
    "PostGIS_AddBBox",
    "PostGIS_DropBBox",
    "PostGIS_HasBBox",
    "ST_3DArea",
    "ST_3DClosestPoint",
    "ST_3DDifference",
    "ST_3DDistance",
    "ST_3DExtent",
    "ST_3DIntersection",
    "ST_3DLength",
    "ST_3DLineInterpolatePoint",
    "ST_3DLongestLine",
    "ST_3DMakeBox",
    "ST_3DMaxDistance",
    "ST_3DPerimeter",
    "ST_3DShortestLine",
    "ST_3DUnion",
    "ST_AddMeasure",
    "ST_AddPoint",
    "ST_Affine",
    "ST_Angle",
    "ST_ApproximateMedialAxis",
    "ST_Area",
    "ST_Azimuth",
    "ST_Boundary",
    "ST_BoundingDiagonal",
    "ST_Buffer",
    "ST_BuildArea",
    "ST_CPAWithin",
    "ST_Centroid",
    "ST_ChaikinSmoothing",
    "ST_ClipByBox2D",
    "ST_ClosestPoint",
    "ST_ClosestPointOfApproach",
    "ST_ClusterDBSCAN",
    "ST_ClusterIntersecting",
    "ST_ClusterKMeans",
    "ST_ClusterWithin",
    "ST_Collect",
    "ST_CollectionExtract",
    "ST_CollectionHomogenize",
    "ST_ConcaveHull",
    "ST_ConstrainedDelaunayTriangles",
    "ST_ConvexHull",
    "ST_CoordDim",
    "ST_CurveToLine",
    "ST_DelaunayTriangles",
    "ST_Difference",
    "ST_Dimension",
    "ST_Distance",
    "ST_DistanceCPA",
    "ST_DistanceSphere",
    "ST_DistanceSpheroid",
    "ST_Dump",
    "ST_DumpPoints",
    "ST_DumpRings",
    "ST_EndPoint",
    "ST_Envelope",
    "ST_EstimatedExtent",
    "ST_Expand",
    "ST_Extent",
    "ST_ExteriorRing",
    "ST_Extrude",
    "ST_FilterByM",
    "ST_FlipCoordinates",
    "ST_Force2D",
    "ST_ForceCurve",
    "ST_ForceLHR",
    "ST_ForcePolygonCCW",
    "ST_ForcePolygonCW",
    "ST_ForceRHR",
    "ST_ForceSFS",
    "ST_Force3D",
    "ST_Force3DM",
    "ST_Force3DZ",
    "ST_Force4D",
    "ST_ForceCollection",
    "ST_FrechetDistance",
    "ST_GeneratePoints",
    "ST_GeometricMedian",
    "ST_GeometryN",
    "ST_GeometryType",
    "ST_HasArc",
    "ST_HausdorffDistance",
    "ST_InteriorRingN",
    "ST_InterpolatePoint",
    "ST_Intersection",
    "ST_IsClosed",
    "ST_IsCollection",
    "ST_IsEmpty",
    "ST_IsPlanar",
    "ST_IsPolygonCCW",
    "ST_IsPolygonCW",
    "ST_IsRing",
    "ST_IsSimple",
    "ST_IsSolid",
    "ST_IsValid",
    "ST_IsValidDetail",
    "ST_IsValidReason",
    "ST_IsValidTrajectory",
    "ST_Length",
    "ST_Length2D",
    "ST_LengthSpheroid",
    "ST_LineFromMultiPoint",
    "ST_LineInterpolatePoint",
    "ST_LineInterpolatePoints",
    "ST_LineLocatePoint",
    "ST_LineMerge",
    "ST_LineSubstring",
    "ST_LineToCurve",
    "ST_LocateAlong",
    "ST_LocateBetween",
    "ST_LocateBetweenElevations",
    "ST_LongestLine",
    "ST_M",
    "ST_MakeBox2D",
    "ST_MakeEnvelope",
    "ST_MakeLine",
    "ST_MakePoint",
    "ST_MakePointM",
    "ST_MakePolygon",
    "ST_MakeSolid",
    "ST_MakeValid",
    "ST_MaxDistance",
    "ST_MemSize",
    "ST_MemUnion",
    "ST_MinimumBoundingCircle",
    "ST_MinimumBoundingRadius",
    "ST_MinimumClearance",
    "ST_MinimumClearanceLine",
    "ST_MinkowskiSum",
    "ST_Multi",
    "ST_NDims",
    "ST_NPoints",
    "ST_NRings",
    "ST_Node",
    "ST_Normalize",
    "ST_NumGeometries",
    "ST_NumInteriorRing",
    "ST_NumInteriorRings",
    "ST_NumPatches",
    "ST_NumPoints",
    "ST_OffsetCurve",
    "ST_Orientation",
    "ST_OrientedEnvelope",
    "ST_PatchN",
    "ST_Perimeter",
    "ST_Perimeter2D",
    "ST_Point",
    "ST_PointN",
    "ST_PointOnSurface",
    "ST_Points",
    "ST_Polygon",
    "ST_Polygonize",
    "ST_Project",
    "ST_QuantizeCoordinates",
    "ST_RemovePoint",
    "ST_RemoveRepeatedPoints",
    "ST_Reverse",
    "ST_Rotate",
    "ST_RotateX",
    "ST_RotateY",
    "ST_RotateZ",
    "ST_SRID",
    "ST_Scale",
    "ST_Segmentize",
    "ST_SetEffectiveArea",
    "ST_SetPoint",
    "ST_SetSRID",
    "ST_SharedPaths",
    "ST_ShiftLongitude",
    "ST_ShortestLine",
    "ST_Simplify",
    "ST_SimplifyPreserveTopology",
    "ST_SimplifyVW",
    "ST_Snap",
    "ST_SnapToGrid",
    "ST_Split",
    "ST_StartPoint",
    "ST_StraightSkeleton",
    "ST_Subdivide",
    "ST_Summary",
    "ST_SwapOrdinates",
    "ST_SymDifference",
    "ST_Tesselate",
    "ST_TileEnvelope",
    "ST_TransScale",
    "ST_Transform",
    "ST_Translate",
    "ST_UnaryUnion",
    "ST_Union",
    "ST_Volume",
    "ST_VoronoiLines",
    "ST_VoronoiPolygons",
    "ST_WrapX",
    "ST_X",
    "ST_XMax",
    "ST_XMin",
    "ST_Y",
    "ST_YMax",
    "ST_YMin",
    "ST_Z",
    "ST_ZMax",
    "ST_ZMin",
    "ST_Zmflag",
]
