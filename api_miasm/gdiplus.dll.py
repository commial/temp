
def gdiplus_GdiplusStartup(jitter):
    """"
    [gdiplus.dll] GpStatus GdiplusStartup(ULONG_PTR* token, const GdiplusStartupInput* input, GdiplusStartupOutput* output)
    """"
    ret_ad, args = jitter.func_args_stdcall(["token", "input", "output"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdiplusShutdown(jitter):
    """"
    [gdiplus.dll] void GdiplusShutdown(ULONG_PTR token)
    """"
    ret_ad, args = jitter.func_args_stdcall(["token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePath(GpFillMode brushMode, GpPath** path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brushMode", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePath2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePath2(GDIPCONST GpPointF* points, GDIPCONST PathPointType* types, INT count, GpFillMode fillMode, GpPath** path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["points", "types", "count", "fillMode", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePath2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePath2I(GDIPCONST GpPoint* points, GDIPCONST PathPointType* types, INT count, GpFillMode fillMode, GpPath** path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["points", "types", "count", "fillMode", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipClonePath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipClonePath(GpPath* path, GpPath** clonePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "clonePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeletePath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeletePath(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetPath(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPointCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPointCount(GpPath* path, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathTypes(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathTypes(GpPath* path, PathPointType* types, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "types", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathPoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathPoints(GpPath* path, GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathPointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathPointsI(GpPath* path, GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathFillMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathFillMode(GpPath* path, GpFillMode* fillmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "fillmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathFillMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathFillMode(GpPath* path, GpFillMode fillmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "fillmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathData(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathData(GpPath* path, GpPathData* pathData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "pathData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipStartPathFigure(jitter):
    """"
    [gdiplus.dll] GpStatus GdipStartPathFigure(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipClosePathFigure(jitter):
    """"
    [gdiplus.dll] GpStatus GdipClosePathFigure(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipClosePathFigures(jitter):
    """"
    [gdiplus.dll] GpStatus GdipClosePathFigures(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathMarker(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathMarker(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipClearPathMarkers(jitter):
    """"
    [gdiplus.dll] GpStatus GdipClearPathMarkers(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipReversePath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipReversePath(GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathLastPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathLastPoint(GpPath* path, GpPointF* lastPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "lastPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathLine(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathLine(GpPath* path, REAL x1, REAL y1, REAL x2, REAL y2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x1", "y1", "x2", "y2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathLine2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathLine2(GpPath* path, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathArc(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathArc(GpPath* path, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathBezier(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathBezier(GpPath* path, REAL x1, REAL y1, REAL x2, REAL y2, REAL x3, REAL y3, REAL x4, REAL y4)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathBeziers(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathBeziers(GpPath* path, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathCurve(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathCurve(GpPath* path, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathCurve2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathCurve2(GpPath* path, GDIPCONST GpPointF* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathCurve3(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathCurve3(GpPath* path, GDIPCONST GpPointF* points, INT count, INT offset, INT numberOfSegments, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count", "offset", "numberOfSegments", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathClosedCurve(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathClosedCurve(GpPath* path, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathClosedCurve2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathClosedCurve2(GpPath* path, GDIPCONST GpPointF* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathRectangle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathRectangle(GpPath* path, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathRectangles(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathRectangles(GpPath* path, GDIPCONST GpRectF* rects, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "rects", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathEllipse(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathEllipse(GpPath* path, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathPie(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathPie(GpPath* path, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathPolygon(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathPolygon(GpPath* path, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathPath(GpPath* path, GDIPCONST GpPath* addingPath, BOOL connect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "addingPath", "connect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathString(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathString(GpPath* path, GDIPCONST WCHAR* string, INT length, GDIPCONST GpFontFamily* family, INT style, REAL emSize, GDIPCONST RectF* layoutRect, GDIPCONST GpStringFormat* format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "string", "length", "family", "style", "emSize", "layoutRect", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathStringI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathStringI(GpPath* path, GDIPCONST WCHAR* string, INT length, GDIPCONST GpFontFamily* family, INT style, REAL emSize, GDIPCONST Rect* layoutRect, GDIPCONST GpStringFormat* format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "string", "length", "family", "style", "emSize", "layoutRect", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathLineI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathLineI(GpPath* path, INT x1, INT y1, INT x2, INT y2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x1", "y1", "x2", "y2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathLine2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathLine2I(GpPath* path, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathArcI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathArcI(GpPath* path, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathBezierI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathBezierI(GpPath* path, INT x1, INT y1, INT x2, INT y2, INT x3, INT y3, INT x4, INT y4)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathBeziersI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathBeziersI(GpPath* path, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathCurveI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathCurveI(GpPath* path, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathCurve2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathCurve2I(GpPath* path, GDIPCONST GpPoint* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathCurve3I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathCurve3I(GpPath* path, GDIPCONST GpPoint* points, INT count, INT offset, INT numberOfSegments, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count", "offset", "numberOfSegments", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathClosedCurveI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathClosedCurveI(GpPath* path, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathClosedCurve2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathClosedCurve2I(GpPath* path, GDIPCONST GpPoint* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathRectangleI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathRectangleI(GpPath* path, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathRectanglesI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathRectanglesI(GpPath* path, GDIPCONST GpRect* rects, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "rects", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathEllipseI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathEllipseI(GpPath* path, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathPieI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathPieI(GpPath* path, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipAddPathPolygonI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipAddPathPolygonI(GpPath* path, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFlattenPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFlattenPath(GpPath* path, GpMatrix* matrix, REAL flatness)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "matrix", "flatness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipWindingModeOutline(jitter):
    """"
    [gdiplus.dll] GpStatus GdipWindingModeOutline(GpPath* path, GpMatrix* matrix, REAL flatness)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "matrix", "flatness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipWidenPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipWidenPath(GpPath* nativePath, GpPen* pen, GpMatrix* matrix, REAL flatness)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nativePath", "pen", "matrix", "flatness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipWarpPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipWarpPath(GpPath* path, GpMatrix* matrix, GDIPCONST GpPointF* points, INT count, REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight, WarpMode warpMode, REAL flatness)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "matrix", "points", "count", "srcx", "srcy", "srcwidth", "srcheight", "warpMode", "flatness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTransformPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTransformPath(GpPath* path, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathWorldBounds(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathWorldBounds(GpPath* path, GpRectF* bounds, GDIPCONST GpMatrix* matrix, GDIPCONST GpPen* pen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "bounds", "matrix", "pen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathWorldBoundsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathWorldBoundsI(GpPath* path, GpRect* bounds, GDIPCONST GpMatrix* matrix, GDIPCONST GpPen* pen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "bounds", "matrix", "pen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisiblePathPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisiblePathPoint(GpPath* path, REAL x, REAL y, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisiblePathPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisiblePathPointI(GpPath* path, INT x, INT y, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsOutlineVisiblePathPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsOutlineVisiblePathPoint(GpPath* path, REAL x, REAL y, GpPen* pen, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "pen", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsOutlineVisiblePathPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsOutlineVisiblePathPointI(GpPath* path, INT x, INT y, GpPen* pen, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "x", "y", "pen", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePathIter(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePathIter(GpPathIterator** iterator, GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeletePathIter(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeletePathIter(GpPathIterator* iterator)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterNextSubpath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterNextSubpath(GpPathIterator* iterator, INT* resultCount, INT* startIndex, INT* endIndex, BOOL* isClosed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "startIndex", "endIndex", "isClosed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterNextSubpathPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterNextSubpathPath(GpPathIterator* iterator, INT* resultCount, GpPath* path, BOOL* isClosed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "path", "isClosed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterNextPathType(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterNextPathType(GpPathIterator* iterator, INT* resultCount, PathPointType* pathType, INT* startIndex, INT* endIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "pathType", "startIndex", "endIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterNextMarker(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterNextMarker(GpPathIterator* iterator, INT* resultCount, INT* startIndex, INT* endIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "startIndex", "endIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterNextMarkerPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterNextMarkerPath(GpPathIterator* iterator, INT* resultCount, GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterGetCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterGetCount(GpPathIterator* iterator, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterGetSubpathCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterGetSubpathCount(GpPathIterator* iterator, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterIsValid(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterIsValid(GpPathIterator* iterator, BOOL* valid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "valid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterHasCurve(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterHasCurve(GpPathIterator* iterator, BOOL* hasCurve)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "hasCurve"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterRewind(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterRewind(GpPathIterator* iterator)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterEnumerate(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterEnumerate(GpPathIterator* iterator, INT* resultCount, GpPointF* points, PathPointType* types, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "points", "types", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPathIterCopyData(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPathIterCopyData(GpPathIterator* iterator, INT* resultCount, GpPointF* points, PathPointType* types, INT startIndex, INT endIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iterator", "resultCount", "points", "types", "startIndex", "endIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMatrix(GpMatrix** matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMatrix2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMatrix2(REAL m11, REAL m12, REAL m21, REAL m22, REAL dx, REAL dy, GpMatrix** matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["m11", "m12", "m21", "m22", "dx", "dy", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMatrix3(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMatrix3(GDIPCONST GpRectF* rect, GDIPCONST GpPointF* dstplg, GpMatrix** matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "dstplg", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMatrix3I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMatrix3I(GDIPCONST GpRect* rect, GDIPCONST GpPoint* dstplg, GpMatrix** matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "dstplg", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneMatrix(GpMatrix* matrix, GpMatrix** cloneMatrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "cloneMatrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteMatrix(GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetMatrixElements(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetMatrixElements(GpMatrix* matrix, REAL m11, REAL m12, REAL m21, REAL m22, REAL dx, REAL dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "m11", "m12", "m21", "m22", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMultiplyMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMultiplyMatrix(GpMatrix* matrix, GpMatrix* matrix2, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "matrix2", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateMatrix(GpMatrix* matrix, REAL offsetX, REAL offsetY, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "offsetX", "offsetY", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipScaleMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipScaleMatrix(GpMatrix* matrix, REAL scaleX, REAL scaleY, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "scaleX", "scaleY", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRotateMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRotateMatrix(GpMatrix* matrix, REAL angle, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "angle", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipShearMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipShearMatrix(GpMatrix* matrix, REAL shearX, REAL shearY, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "shearX", "shearY", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipInvertMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipInvertMatrix(GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTransformMatrixPoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTransformMatrixPoints(GpMatrix* matrix, GpPointF* pts, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "pts", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTransformMatrixPointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTransformMatrixPointsI(GpMatrix* matrix, GpPoint* pts, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "pts", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipVectorTransformMatrixPoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipVectorTransformMatrixPoints(GpMatrix* matrix, GpPointF* pts, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "pts", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipVectorTransformMatrixPointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipVectorTransformMatrixPointsI(GpMatrix* matrix, GpPoint* pts, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "pts", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMatrixElements(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMatrixElements(GDIPCONST GpMatrix* matrix, REAL* matrixOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "matrixOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsMatrixInvertible(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsMatrixInvertible(GDIPCONST GpMatrix* matrix, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsMatrixIdentity(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsMatrixIdentity(GDIPCONST GpMatrix* matrix, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsMatrixEqual(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsMatrixEqual(GDIPCONST GpMatrix* matrix, GDIPCONST GpMatrix* matrix2, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["matrix", "matrix2", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateRegion(GpRegion** region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateRegionRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateRegionRect(GDIPCONST GpRectF* rect, GpRegion** region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateRegionRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateRegionRectI(GDIPCONST GpRect* rect, GpRegion** region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateRegionPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateRegionPath(GpPath* path, GpRegion** region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateRegionRgnData(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateRegionRgnData(GDIPCONST BYTE* regionData, INT size, GpRegion** region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["regionData", "size", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateRegionHrgn(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateRegionHrgn(HRGN hRgn, GpRegion** region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRgn", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneRegion(GpRegion* region, GpRegion** cloneRegion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "cloneRegion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteRegion(GpRegion* region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetInfinite(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetInfinite(GpRegion* region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetEmpty(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetEmpty(GpRegion* region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCombineRegionRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCombineRegionRect(GpRegion* region, GDIPCONST GpRectF* rect, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "rect", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCombineRegionRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCombineRegionRectI(GpRegion* region, GDIPCONST GpRect* rect, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "rect", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCombineRegionPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCombineRegionPath(GpRegion* region, GpPath* path, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "path", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCombineRegionRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCombineRegionRegion(GpRegion* region, GpRegion* region2, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "region2", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateRegion(GpRegion* region, REAL dx, REAL dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateRegionI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateRegionI(GpRegion* region, INT dx, INT dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTransformRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTransformRegion(GpRegion* region, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionBounds(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionBounds(GpRegion* region, GpGraphics* graphics, GpRectF* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "graphics", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionBoundsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionBoundsI(GpRegion* region, GpGraphics* graphics, GpRect* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "graphics", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionHRgn(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionHRgn(GpRegion* region, GpGraphics* graphics, HRGN* hRgn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "graphics", "hRgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsEmptyRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsEmptyRegion(GpRegion* region, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsInfiniteRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsInfiniteRegion(GpRegion* region, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsEqualRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsEqualRegion(GpRegion* region, GpRegion* region2, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "region2", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionDataSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionDataSize(GpRegion* region, UINT* bufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "bufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionData(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionData(GpRegion* region, BYTE* buffer, UINT bufferSize, UINT* sizeFilled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "buffer", "bufferSize", "sizeFilled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleRegionPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleRegionPoint(GpRegion* region, REAL x, REAL y, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "x", "y", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleRegionPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleRegionPointI(GpRegion* region, INT x, INT y, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "x", "y", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleRegionRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleRegionRect(GpRegion* region, REAL x, REAL y, REAL width, REAL height, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "x", "y", "width", "height", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleRegionRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleRegionRectI(GpRegion* region, INT x, INT y, INT width, INT height, GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "x", "y", "width", "height", "graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionScansCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionScansCount(GpRegion* region, UINT* count, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "count", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionScans(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionScans(GpRegion* region, GpRectF* rects, INT* count, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "rects", "count", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRegionScansI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRegionScansI(GpRegion* region, GpRect* rects, INT* count, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["region", "rects", "count", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneBrush(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneBrush(GpBrush* brush, GpBrush** cloneBrush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "cloneBrush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteBrush(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteBrush(GpBrush* brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetBrushType(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetBrushType(GpBrush* brush, GpBrushType* type)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateHatchBrush(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateHatchBrush(GpHatchStyle hatchstyle, ARGB forecol, ARGB backcol, GpHatch** brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hatchstyle", "forecol", "backcol", "brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetHatchStyle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetHatchStyle(GpHatch* brush, GpHatchStyle* hatchstyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "hatchstyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetHatchForegroundColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetHatchForegroundColor(GpHatch* brush, ARGB* forecol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "forecol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetHatchBackgroundColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetHatchBackgroundColor(GpHatch* brush, ARGB* backcol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "backcol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateTexture(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateTexture(GpImage* image, GpWrapMode wrapmode, GpTexture** texture)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "wrapmode", "texture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateTexture2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateTexture2(GpImage* image, GpWrapMode wrapmode, REAL x, REAL y, REAL width, REAL height, GpTexture** texture)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "wrapmode", "x", "y", "width", "height", "texture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateTextureIA(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateTextureIA(GpImage* image, GDIPCONST GpImageAttributes* imageAttributes, REAL x, REAL y, REAL width, REAL height, GpTexture** texture)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "imageAttributes", "x", "y", "width", "height", "texture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateTexture2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateTexture2I(GpImage* image, GpWrapMode wrapmode, INT x, INT y, INT width, INT height, GpTexture** texture)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "wrapmode", "x", "y", "width", "height", "texture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateTextureIAI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateTextureIAI(GpImage* image, GDIPCONST GpImageAttributes* imageAttributes, INT x, INT y, INT width, INT height, GpTexture** texture)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "imageAttributes", "x", "y", "width", "height", "texture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetTextureTransform(GpTexture* brush, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetTextureTransform(GpTexture* brush, GDIPCONST GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetTextureTransform(GpTexture* brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMultiplyTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMultiplyTextureTransform(GpTexture* brush, GDIPCONST GpMatrix* matrix, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateTextureTransform(GpTexture* brush, REAL dx, REAL dy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "dx", "dy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipScaleTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipScaleTextureTransform(GpTexture* brush, REAL sx, REAL sy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "sx", "sy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRotateTextureTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRotateTextureTransform(GpTexture* brush, REAL angle, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "angle", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetTextureWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetTextureWrapMode(GpTexture* brush, GpWrapMode wrapmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "wrapmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetTextureWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetTextureWrapMode(GpTexture* brush, GpWrapMode* wrapmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "wrapmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetTextureImage(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetTextureImage(GpTexture* brush, GpImage** image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateSolidFill(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateSolidFill(ARGB color, GpSolidFill** brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["color", "brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetSolidFillColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetSolidFillColor(GpSolidFill* brush, ARGB color)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "color"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetSolidFillColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetSolidFillColor(GpSolidFill* brush, ARGB* color)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "color"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateLineBrush(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateLineBrush(GDIPCONST GpPointF* point1, GDIPCONST GpPointF* point2, ARGB color1, ARGB color2, GpWrapMode wrapMode, GpLineGradient** lineGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["point1", "point2", "color1", "color2", "wrapMode", "lineGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateLineBrushI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateLineBrushI(GDIPCONST GpPoint* point1, GDIPCONST GpPoint* point2, ARGB color1, ARGB color2, GpWrapMode wrapMode, GpLineGradient** lineGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["point1", "point2", "color1", "color2", "wrapMode", "lineGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateLineBrushFromRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateLineBrushFromRect(GDIPCONST GpRectF* rect, ARGB color1, ARGB color2, LinearGradientMode mode, GpWrapMode wrapMode, GpLineGradient** lineGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "color1", "color2", "mode", "wrapMode", "lineGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateLineBrushFromRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateLineBrushFromRectI(GDIPCONST GpRect* rect, ARGB color1, ARGB color2, LinearGradientMode mode, GpWrapMode wrapMode, GpLineGradient** lineGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "color1", "color2", "mode", "wrapMode", "lineGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateLineBrushFromRectWithAngle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateLineBrushFromRectWithAngle(GDIPCONST GpRectF* rect, ARGB color1, ARGB color2, REAL angle, BOOL isAngleScalable, GpWrapMode wrapMode, GpLineGradient** lineGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "color1", "color2", "angle", "isAngleScalable", "wrapMode", "lineGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateLineBrushFromRectWithAngleI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateLineBrushFromRectWithAngleI(GDIPCONST GpRect* rect, ARGB color1, ARGB color2, REAL angle, BOOL isAngleScalable, GpWrapMode wrapMode, GpLineGradient** lineGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rect", "color1", "color2", "angle", "isAngleScalable", "wrapMode", "lineGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineColors(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineColors(GpLineGradient* brush, ARGB color1, ARGB color2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "color1", "color2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineColors(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineColors(GpLineGradient* brush, ARGB* colors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "colors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineRect(GpLineGradient* brush, GpRectF* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineRectI(GpLineGradient* brush, GpRect* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineGammaCorrection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineGammaCorrection(GpLineGradient* brush, BOOL useGammaCorrection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "useGammaCorrection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineGammaCorrection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineGammaCorrection(GpLineGradient* brush, BOOL* useGammaCorrection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "useGammaCorrection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineBlendCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineBlendCount(GpLineGradient* brush, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineBlend(GpLineGradient* brush, REAL* blend, REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineBlend(GpLineGradient* brush, GDIPCONST REAL* blend, GDIPCONST REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLinePresetBlendCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLinePresetBlendCount(GpLineGradient* brush, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLinePresetBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLinePresetBlend(GpLineGradient* brush, ARGB* blend, REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLinePresetBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLinePresetBlend(GpLineGradient* brush, GDIPCONST ARGB* blend, GDIPCONST REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineSigmaBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineSigmaBlend(GpLineGradient* brush, REAL focus, REAL scale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "focus", "scale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineLinearBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineLinearBlend(GpLineGradient* brush, REAL focus, REAL scale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "focus", "scale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineWrapMode(GpLineGradient* brush, GpWrapMode wrapmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "wrapmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineWrapMode(GpLineGradient* brush, GpWrapMode* wrapmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "wrapmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineTransform(GpLineGradient* brush, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetLineTransform(GpLineGradient* brush, GDIPCONST GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetLineTransform(GpLineGradient* brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMultiplyLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMultiplyLineTransform(GpLineGradient* brush, GDIPCONST GpMatrix* matrix, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateLineTransform(GpLineGradient* brush, REAL dx, REAL dy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "dx", "dy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipScaleLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipScaleLineTransform(GpLineGradient* brush, REAL sx, REAL sy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "sx", "sy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRotateLineTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRotateLineTransform(GpLineGradient* brush, REAL angle, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "angle", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePathGradient(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePathGradient(GDIPCONST GpPointF* points, INT count, GpWrapMode wrapMode, GpPathGradient** polyGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["points", "count", "wrapMode", "polyGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePathGradientI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePathGradientI(GDIPCONST GpPoint* points, INT count, GpWrapMode wrapMode, GpPathGradient** polyGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["points", "count", "wrapMode", "polyGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePathGradientFromPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePathGradientFromPath(GDIPCONST GpPath* path, GpPathGradient** polyGradient)
    """"
    ret_ad, args = jitter.func_args_stdcall(["path", "polyGradient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientCenterColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientCenterColor(GpPathGradient* brush, ARGB* colors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "colors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientCenterColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientCenterColor(GpPathGradient* brush, ARGB colors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "colors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientSurroundColorsWithCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientSurroundColorsWithCount(GpPathGradient* brush, ARGB* color, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "color", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientSurroundColorsWithCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientSurroundColorsWithCount(GpPathGradient* brush, GDIPCONST ARGB* color, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "color", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientPath(GpPathGradient* brush, GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientPath(GpPathGradient* brush, GDIPCONST GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientCenterPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientCenterPoint(GpPathGradient* brush, GpPointF* points)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "points"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientCenterPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientCenterPointI(GpPathGradient* brush, GpPoint* points)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "points"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientCenterPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientCenterPoint(GpPathGradient* brush, GDIPCONST GpPointF* points)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "points"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientCenterPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientCenterPointI(GpPathGradient* brush, GDIPCONST GpPoint* points)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "points"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientRect(GpPathGradient* brush, GpRectF* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientRectI(GpPathGradient* brush, GpRect* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientPointCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientPointCount(GpPathGradient* brush, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientSurroundColorCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientSurroundColorCount(GpPathGradient* brush, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientGammaCorrection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientGammaCorrection(GpPathGradient* brush, BOOL useGammaCorrection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "useGammaCorrection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientGammaCorrection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientGammaCorrection(GpPathGradient* brush, BOOL* useGammaCorrection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "useGammaCorrection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientBlendCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientBlendCount(GpPathGradient* brush, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientBlend(GpPathGradient* brush, REAL* blend, REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientBlend(GpPathGradient* brush, GDIPCONST REAL* blend, GDIPCONST REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientPresetBlendCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientPresetBlendCount(GpPathGradient* brush, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientPresetBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientPresetBlend(GpPathGradient* brush, ARGB* blend, REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientPresetBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientPresetBlend(GpPathGradient* brush, GDIPCONST ARGB* blend, GDIPCONST REAL* positions, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "blend", "positions", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientSigmaBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientSigmaBlend(GpPathGradient* brush, REAL focus, REAL scale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "focus", "scale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientLinearBlend(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientLinearBlend(GpPathGradient* brush, REAL focus, REAL scale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "focus", "scale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientWrapMode(GpPathGradient* brush, GpWrapMode* wrapmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "wrapmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientWrapMode(GpPathGradient* brush, GpWrapMode wrapmode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "wrapmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientTransform(GpPathGradient* brush, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientTransform(GpPathGradient* brush, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetPathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetPathGradientTransform(GpPathGradient* brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMultiplyPathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMultiplyPathGradientTransform(GpPathGradient* brush, GDIPCONST GpMatrix* matrix, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "matrix", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslatePathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslatePathGradientTransform(GpPathGradient* brush, REAL dx, REAL dy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "dx", "dy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipScalePathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipScalePathGradientTransform(GpPathGradient* brush, REAL sx, REAL sy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "sx", "sy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRotatePathGradientTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRotatePathGradientTransform(GpPathGradient* brush, REAL angle, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "angle", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPathGradientFocusScales(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPathGradientFocusScales(GpPathGradient* brush, REAL* xScale, REAL* yScale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "xScale", "yScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPathGradientFocusScales(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPathGradientFocusScales(GpPathGradient* brush, REAL xScale, REAL yScale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "xScale", "yScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePen1(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePen1(ARGB color, REAL width, GpUnit unit, GpPen** pen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["color", "width", "unit", "pen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreatePen2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreatePen2(GpBrush* brush, REAL width, GpUnit unit, GpPen** pen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["brush", "width", "unit", "pen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipClonePen(jitter):
    """"
    [gdiplus.dll] GpStatus GdipClonePen(GpPen* pen, GpPen** clonepen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "clonepen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeletePen(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeletePen(GpPen* pen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenWidth(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenWidth(GpPen* pen, REAL width)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "width"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenWidth(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenWidth(GpPen* pen, REAL* width)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "width"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenUnit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenUnit(GpPen* pen, GpUnit unit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "unit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenUnit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenUnit(GpPen* pen, GpUnit* unit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "unit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenLineCap197819(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenLineCap197819(GpPen* pen, GpLineCap startCap, GpLineCap endCap, GpDashCap dashCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "startCap", "endCap", "dashCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenStartCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenStartCap(GpPen* pen, GpLineCap startCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "startCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenEndCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenEndCap(GpPen* pen, GpLineCap endCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "endCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenDashCap197819(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenDashCap197819(GpPen* pen, GpDashCap dashCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dashCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenStartCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenStartCap(GpPen* pen, GpLineCap* startCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "startCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenEndCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenEndCap(GpPen* pen, GpLineCap* endCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "endCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenDashCap197819(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenDashCap197819(GpPen* pen, GpDashCap* dashCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dashCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenLineJoin(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenLineJoin(GpPen* pen, GpLineJoin lineJoin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "lineJoin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenLineJoin(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenLineJoin(GpPen* pen, GpLineJoin* lineJoin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "lineJoin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenCustomStartCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenCustomStartCap(GpPen* pen, GpCustomLineCap* customCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "customCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenCustomStartCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenCustomStartCap(GpPen* pen, GpCustomLineCap** customCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "customCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenCustomEndCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenCustomEndCap(GpPen* pen, GpCustomLineCap* customCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "customCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenCustomEndCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenCustomEndCap(GpPen* pen, GpCustomLineCap** customCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "customCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenMiterLimit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenMiterLimit(GpPen* pen, REAL miterLimit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "miterLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenMiterLimit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenMiterLimit(GpPen* pen, REAL* miterLimit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "miterLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenMode(GpPen* pen, GpPenAlignment penMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "penMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenMode(GpPen* pen, GpPenAlignment* penMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "penMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenTransform(GpPen* pen, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenTransform(GpPen* pen, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetPenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetPenTransform(GpPen* pen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMultiplyPenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMultiplyPenTransform(GpPen* pen, GDIPCONST GpMatrix* matrix, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "matrix", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslatePenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslatePenTransform(GpPen* pen, REAL dx, REAL dy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dx", "dy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipScalePenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipScalePenTransform(GpPen* pen, REAL sx, REAL sy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "sx", "sy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRotatePenTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRotatePenTransform(GpPen* pen, REAL angle, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "angle", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenColor(GpPen* pen, ARGB argb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "argb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenColor(GpPen* pen, ARGB* argb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "argb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenBrushFill(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenBrushFill(GpPen* pen, GpBrush* brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenBrushFill(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenBrushFill(GpPen* pen, GpBrush** brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenFillType(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenFillType(GpPen* pen, GpPenType* type)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenDashStyle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenDashStyle(GpPen* pen, GpDashStyle* dashstyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dashstyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenDashStyle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenDashStyle(GpPen* pen, GpDashStyle dashstyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dashstyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenDashOffset(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenDashOffset(GpPen* pen, REAL* offset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenDashOffset(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenDashOffset(GpPen* pen, REAL offset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenDashCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenDashCount(GpPen* pen, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenDashArray(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenDashArray(GpPen* pen, GDIPCONST REAL* dash, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dash", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenDashArray(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenDashArray(GpPen* pen, REAL* dash, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dash", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenCompoundCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenCompoundCount(GpPen* pen, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPenCompoundArray(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPenCompoundArray(GpPen* pen, GDIPCONST REAL* dash, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dash", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPenCompoundArray(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPenCompoundArray(GpPen* pen, REAL* dash, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pen", "dash", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateCustomLineCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateCustomLineCap(GpPath* fillPath, GpPath* strokePath, GpLineCap baseCap, REAL baseInset, GpCustomLineCap** customCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fillPath", "strokePath", "baseCap", "baseInset", "customCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteCustomLineCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteCustomLineCap(GpCustomLineCap* customCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneCustomLineCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneCustomLineCap(GpCustomLineCap* customCap, GpCustomLineCap** clonedCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "clonedCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCustomLineCapType(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCustomLineCapType(GpCustomLineCap* customCap, CustomLineCapType* capType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "capType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCustomLineCapStrokeCaps(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCustomLineCapStrokeCaps(GpCustomLineCap* customCap, GpLineCap startCap, GpLineCap endCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "startCap", "endCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCustomLineCapStrokeCaps(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCustomLineCapStrokeCaps(GpCustomLineCap* customCap, GpLineCap* startCap, GpLineCap* endCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "startCap", "endCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCustomLineCapStrokeJoin(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCustomLineCapStrokeJoin(GpCustomLineCap* customCap, GpLineJoin lineJoin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "lineJoin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCustomLineCapStrokeJoin(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCustomLineCapStrokeJoin(GpCustomLineCap* customCap, GpLineJoin* lineJoin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "lineJoin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCustomLineCapBaseCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCustomLineCapBaseCap(GpCustomLineCap* customCap, GpLineCap baseCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "baseCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCustomLineCapBaseCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCustomLineCapBaseCap(GpCustomLineCap* customCap, GpLineCap* baseCap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "baseCap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCustomLineCapBaseInset(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCustomLineCapBaseInset(GpCustomLineCap* customCap, REAL inset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "inset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCustomLineCapBaseInset(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCustomLineCapBaseInset(GpCustomLineCap* customCap, REAL* inset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "inset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCustomLineCapWidthScale(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCustomLineCapWidthScale(GpCustomLineCap* customCap, REAL widthScale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "widthScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCustomLineCapWidthScale(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCustomLineCapWidthScale(GpCustomLineCap* customCap, REAL* widthScale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["customCap", "widthScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateAdjustableArrowCap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateAdjustableArrowCap(REAL height, REAL width, BOOL isFilled, GpAdjustableArrowCap** cap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["height", "width", "isFilled", "cap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetAdjustableArrowCapHeight(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetAdjustableArrowCapHeight(GpAdjustableArrowCap* cap, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetAdjustableArrowCapHeight(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetAdjustableArrowCapHeight(GpAdjustableArrowCap* cap, REAL* height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetAdjustableArrowCapWidth(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetAdjustableArrowCapWidth(GpAdjustableArrowCap* cap, REAL width)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "width"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetAdjustableArrowCapWidth(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetAdjustableArrowCapWidth(GpAdjustableArrowCap* cap, REAL* width)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "width"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetAdjustableArrowCapMiddleInset(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetAdjustableArrowCapMiddleInset(GpAdjustableArrowCap* cap, REAL middleInset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "middleInset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetAdjustableArrowCapMiddleInset(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetAdjustableArrowCapMiddleInset(GpAdjustableArrowCap* cap, REAL* middleInset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "middleInset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetAdjustableArrowCapFillState(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetAdjustableArrowCapFillState(GpAdjustableArrowCap* cap, BOOL fillState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "fillState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetAdjustableArrowCapFillState(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetAdjustableArrowCapFillState(GpAdjustableArrowCap* cap, BOOL* fillState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cap", "fillState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipLoadImageFromStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipLoadImageFromStream(IStream* stream, GpImage** image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipLoadImageFromFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipLoadImageFromFile(GDIPCONST WCHAR* filename, GpImage** image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["filename", "image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipLoadImageFromStreamICM(jitter):
    """"
    [gdiplus.dll] GpStatus GdipLoadImageFromStreamICM(IStream* stream, GpImage** image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipLoadImageFromFileICM(jitter):
    """"
    [gdiplus.dll] GpStatus GdipLoadImageFromFileICM(GDIPCONST WCHAR* filename, GpImage** image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["filename", "image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneImage(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneImage(GpImage* image, GpImage** cloneImage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "cloneImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDisposeImage(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDisposeImage(GpImage* image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSaveImageToFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSaveImageToFile(GpImage* image, GDIPCONST WCHAR* filename, GDIPCONST CLSID* clsidEncoder, GDIPCONST EncoderParameters* encoderParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "filename", "clsidEncoder", "encoderParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSaveImageToStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSaveImageToStream(GpImage* image, IStream* stream, GDIPCONST CLSID* clsidEncoder, GDIPCONST EncoderParameters* encoderParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "stream", "clsidEncoder", "encoderParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSaveAdd(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSaveAdd(GpImage* image, GDIPCONST EncoderParameters* encoderParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "encoderParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSaveAddImage(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSaveAddImage(GpImage* image, GpImage* newImage, GDIPCONST EncoderParameters* encoderParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "newImage", "encoderParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageGraphicsContext(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageGraphicsContext(GpImage* image, GpGraphics** graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageBounds(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageBounds(GpImage* image, GpRectF* srcRect, GpUnit* srcUnit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "srcRect", "srcUnit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageDimension(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageDimension(GpImage* image, REAL* width, REAL* height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageType(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageType(GpImage* image, ImageType* type)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageWidth(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageWidth(GpImage* image, UINT* width)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "width"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageHeight(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageHeight(GpImage* image, UINT* height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageHorizontalResolution(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageHorizontalResolution(GpImage* image, REAL* resolution)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "resolution"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageVerticalResolution(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageVerticalResolution(GpImage* image, REAL* resolution)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "resolution"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageFlags(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageFlags(GpImage* image, UINT* flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageRawFormat(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageRawFormat(GpImage* image, GUID* format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImagePixelFormat(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImagePixelFormat(GpImage* image, PixelFormat* format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageThumbnail(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageThumbnail(GpImage* image, UINT thumbWidth, UINT thumbHeight, GpImage** thumbImage, GetThumbnailImageAbort callback, VOID* callbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "thumbWidth", "thumbHeight", "thumbImage", "callback", "callbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetEncoderParameterListSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetEncoderParameterListSize(GpImage* image, GDIPCONST CLSID* clsidEncoder, UINT* size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "clsidEncoder", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetEncoderParameterList(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetEncoderParameterList(GpImage* image, GDIPCONST CLSID* clsidEncoder, UINT size, EncoderParameters* buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "clsidEncoder", "size", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageGetFrameDimensionsCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageGetFrameDimensionsCount(GpImage* image, UINT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageGetFrameDimensionsList(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageGetFrameDimensionsList(GpImage* image, GUID* dimensionIDs, UINT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "dimensionIDs", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageGetFrameCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageGetFrameCount(GpImage* image, GDIPCONST GUID* dimensionID, UINT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "dimensionID", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageSelectActiveFrame(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageSelectActiveFrame(GpImage* image, GDIPCONST GUID* dimensionID, UINT frameIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "dimensionID", "frameIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageRotateFlip(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageRotateFlip(GpImage* image, RotateFlipType rfType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "rfType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImagePalette(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImagePalette(GpImage* image, ColorPalette* palette, INT size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "palette", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImagePalette(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImagePalette(GpImage* image, GDIPCONST ColorPalette* palette)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "palette"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImagePaletteSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImagePaletteSize(GpImage* image, INT* size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPropertyCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPropertyCount(GpImage* image, UINT* numOfProperty)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "numOfProperty"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPropertyIdList(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPropertyIdList(GpImage* image, UINT numOfProperty, PROPID* list)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "numOfProperty", "list"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPropertyItemSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPropertyItemSize(GpImage* image, PROPID propId, UINT* size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "propId", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPropertyItem(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPropertyItem(GpImage* image, PROPID propId, PropertyItem* buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "propId", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPropertySize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPropertySize(GpImage* image, UINT* totalBufferSize, UINT* numProperties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "totalBufferSize", "numProperties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetAllPropertyItems(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetAllPropertyItems(GpImage* image, UINT totalBufferSize, UINT numProperties, PropertyItem* allItems)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "totalBufferSize", "numProperties", "allItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRemovePropertyItem(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRemovePropertyItem(GpImage* image, PROPID propId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "propId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPropertyItem(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPropertyItem(GpImage* image, GDIPCONST PropertyItem* item)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "item"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFindFirstImageItem(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFindFirstImageItem(GpImage* image, ImageItemData* item)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "item"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFindNextImageItem(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFindNextImageItem(GpImage* image, ImageItemData* item)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "item"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageItemData(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageItemData(GpImage* image, ImageItemData* item)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image", "item"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageForceValidation(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageForceValidation(GpImage* image)
    """"
    ret_ad, args = jitter.func_args_stdcall(["image"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromStream(IStream* stream, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromFile(GDIPCONST WCHAR* filename, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["filename", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromStreamICM(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromStreamICM(IStream* stream, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromFileICM(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromFileICM(GDIPCONST WCHAR* filename, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["filename", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromScan0(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromScan0(INT width, INT height, INT stride, PixelFormat format, BYTE* scan0, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["width", "height", "stride", "format", "scan0", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromGraphics(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromGraphics(INT width, INT height, GpGraphics* target, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["width", "height", "target", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromDirectDrawSurface(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromDirectDrawSurface(IDirectDrawSurface7* surface, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["surface", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromGdiDib(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromGdiDib(GDIPCONST BITMAPINFO* gdiBitmapInfo, VOID* gdiBitmapData, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["gdiBitmapInfo", "gdiBitmapData", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromHBITMAP(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromHBITMAP(HBITMAP hbm, HPALETTE hpal, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbm", "hpal", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateHBITMAPFromBitmap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateHBITMAPFromBitmap(GpBitmap* bitmap, HBITMAP* hbmReturn, ARGB background)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "hbmReturn", "background"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromHICON(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromHICON(HICON hicon, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hicon", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateHICONFromBitmap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateHICONFromBitmap(GpBitmap* bitmap, HICON* hbmReturn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "hbmReturn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateBitmapFromResource(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateBitmapFromResource(HINSTANCE hInstance, GDIPCONST WCHAR* lpBitmapName, GpBitmap** bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpBitmapName", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneBitmapArea(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneBitmapArea(REAL x, REAL y, REAL width, REAL height, PixelFormat format, GpBitmap* srcBitmap, GpBitmap** dstBitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["x", "y", "width", "height", "format", "srcBitmap", "dstBitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneBitmapAreaI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneBitmapAreaI(INT x, INT y, INT width, INT height, PixelFormat format, GpBitmap* srcBitmap, GpBitmap** dstBitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["x", "y", "width", "height", "format", "srcBitmap", "dstBitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapLockBits(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapLockBits(GpBitmap* bitmap, GDIPCONST GpRect* rect, [ImageLockMode] flags, PixelFormat format, BitmapData* lockedBitmapData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "rect", "flags", "format", "lockedBitmapData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapUnlockBits(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapUnlockBits(GpBitmap* bitmap, BitmapData* lockedBitmapData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "lockedBitmapData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapGetPixel(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapGetPixel(GpBitmap* bitmap, INT x, INT y, ARGB* color)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "x", "y", "color"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapSetPixel(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapSetPixel(GpBitmap* bitmap, INT x, INT y, ARGB color)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "x", "y", "color"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipImageSetAbort(jitter):
    """"
    [gdiplus.dll] GpStatus GdipImageSetAbort(GpImage* pImage, GdiplusAbort* pIAbort)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pImage", "pIAbort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGraphicsSetAbort(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGraphicsSetAbort(GpGraphics* pGraphics, GdiplusAbort* pIAbort)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGraphics", "pIAbort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapConvertFormat(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapConvertFormat(GpBitmap* pInputBitmap, PixelFormat format, DitherType dithertype, PaletteType palettetype, ColorPalette* palette, REAL alphaThresholdPercent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInputBitmap", "format", "dithertype", "palettetype", "palette", "alphaThresholdPercent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipInitializePalette(jitter):
    """"
    [gdiplus.dll] GpStatus GdipInitializePalette(ColorPalette* palette, PaletteType palettetype, INT optimalColors, BOOL useTransparentColor, GpBitmap* bitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["palette", "palettetype", "optimalColors", "useTransparentColor", "bitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapApplyEffect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapApplyEffect(GpBitmap* bitmap, CGpEffect* effect, RECT* roi, BOOL useAuxData, VOID** auxData, INT* auxDataSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "effect", "roi", "useAuxData", "auxData", "auxDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapCreateApplyEffect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapCreateApplyEffect(GpBitmap** inputBitmaps, INT numInputs, CGpEffect* effect, RECT* roi, RECT* outputRect, GpBitmap** outputBitmap, BOOL useAuxData, VOID** auxData, INT* auxDataSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["inputBitmaps", "numInputs", "effect", "roi", "outputRect", "outputBitmap", "useAuxData", "auxData", "auxDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapGetHistogram(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapGetHistogram(GpBitmap* bitmap, HistogramFormat format, UINT NumberOfEntries, UINT* channel0, UINT* channel1, UINT* channel2, UINT* channel3)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "format", "NumberOfEntries", "channel0", "channel1", "channel2", "channel3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapGetHistogramSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapGetHistogramSize(HistogramFormat format, UINT* NumberOfEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "NumberOfEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBitmapSetResolution(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBitmapSetResolution(GpBitmap* bitmap, REAL xdpi, REAL ydpi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "xdpi", "ydpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateImageAttributes(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateImageAttributes(GpImageAttributes** imageattr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneImageAttributes(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneImageAttributes(GDIPCONST GpImageAttributes* imageattr, GpImageAttributes** cloneImageattr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "cloneImageattr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDisposeImageAttributes(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDisposeImageAttributes(GpImageAttributes* imageattr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesToIdentity(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesToIdentity(GpImageAttributes* imageattr, ColorAdjustType type)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetImageAttributes(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetImageAttributes(GpImageAttributes* imageattr, ColorAdjustType type)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesColorMatrix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesColorMatrix(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, GDIPCONST ColorMatrix* colorMatrix, GDIPCONST ColorMatrix* grayMatrix, ColorMatrixFlags flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "colorMatrix", "grayMatrix", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesThreshold(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesThreshold(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, REAL threshold)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "threshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesGamma(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesGamma(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, REAL gamma)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "gamma"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesNoOp(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesNoOp(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesColorKeys(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesColorKeys(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, ARGB colorLow, ARGB colorHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "colorLow", "colorHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesOutputChannel(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesOutputChannel(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, ColorChannelFlags channelFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "channelFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesOutputChannelColorProfile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesOutputChannelColorProfile(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, GDIPCONST WCHAR* colorProfileFilename)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "colorProfileFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesRemapTable(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesRemapTable(GpImageAttributes* imageattr, ColorAdjustType type, BOOL enableFlag, UINT mapSize, GDIPCONST ColorMap* map)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "type", "enableFlag", "mapSize", "map"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesWrapMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesWrapMode(GpImageAttributes* imageAttr, GpWrapMode wrap, ARGB argb, BOOL clamp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageAttr", "wrap", "argb", "clamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesICMMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesICMMode(GpImageAttributes* imageAttr, BOOL on)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageAttr", "on"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageAttributesAdjustedPalette(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageAttributesAdjustedPalette(GpImageAttributes* imageAttr, ColorPalette* colorPalette, ColorAdjustType colorAdjustType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageAttr", "colorPalette", "colorAdjustType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFlush(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFlush(GpGraphics* graphics, GpFlushIntention intention)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "intention"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFromHDC(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFromHDC(HDC hdc, GpGraphics** graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFromHDC2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFromHDC2(HDC hdc, HANDLE hDevice, GpGraphics** graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hDevice", "graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFromHWND(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFromHWND(HWND hwnd, GpGraphics** graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFromHWNDICM(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFromHWNDICM(HWND hwnd, GpGraphics** graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteGraphics(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteGraphics(GpGraphics* graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetDC(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetDC(GpGraphics* graphics, HDC* hdc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipReleaseDC(jitter):
    """"
    [gdiplus.dll] GpStatus GdipReleaseDC(GpGraphics* graphics, HDC hdc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCompositingMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCompositingMode(GpGraphics* graphics, CompositingMode compositingMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "compositingMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCompositingMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCompositingMode(GpGraphics* graphics, CompositingMode* compositingMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "compositingMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetRenderingOrigin(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetRenderingOrigin(GpGraphics* graphics, INT x, INT y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetRenderingOrigin(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetRenderingOrigin(GpGraphics* graphics, INT* x, INT* y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetCompositingQuality(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetCompositingQuality(GpGraphics* graphics, CompositingQuality compositingQuality)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "compositingQuality"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCompositingQuality(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCompositingQuality(GpGraphics* graphics, CompositingQuality* compositingQuality)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "compositingQuality"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetSmoothingMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetSmoothingMode(GpGraphics* graphics, SmoothingMode smoothingMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "smoothingMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetSmoothingMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetSmoothingMode(GpGraphics* graphics, SmoothingMode* smoothingMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "smoothingMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPixelOffsetMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPixelOffsetMode(GpGraphics* graphics, PixelOffsetMode pixelOffsetMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pixelOffsetMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPixelOffsetMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPixelOffsetMode(GpGraphics* graphics, PixelOffsetMode* pixelOffsetMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pixelOffsetMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetTextRenderingHint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetTextRenderingHint(GpGraphics* graphics, TextRenderingHint mode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetTextRenderingHint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetTextRenderingHint(GpGraphics* graphics, TextRenderingHint* mode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetTextContrast(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetTextContrast(GpGraphics* graphics, UINT contrast)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "contrast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetTextContrast(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetTextContrast(GpGraphics* graphics, UINT* contrast)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "contrast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetInterpolationMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetInterpolationMode(GpGraphics* graphics, InterpolationMode interpolationMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "interpolationMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetInterpolationMode(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetInterpolationMode(GpGraphics* graphics, InterpolationMode* interpolationMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "interpolationMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetWorldTransform(GpGraphics* graphics, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetWorldTransform(GpGraphics* graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMultiplyWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMultiplyWorldTransform(GpGraphics* graphics, GDIPCONST GpMatrix* matrix, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "matrix", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateWorldTransform(GpGraphics* graphics, REAL dx, REAL dy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dx", "dy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipScaleWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipScaleWorldTransform(GpGraphics* graphics, REAL sx, REAL sy, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "sx", "sy", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRotateWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRotateWorldTransform(GpGraphics* graphics, REAL angle, GpMatrixOrder order)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "angle", "order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetWorldTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetWorldTransform(GpGraphics* graphics, GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetPageTransform(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetPageTransform(GpGraphics* graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPageUnit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPageUnit(GpGraphics* graphics, GpUnit* unit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "unit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetPageScale(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetPageScale(GpGraphics* graphics, REAL* scale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "scale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPageUnit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPageUnit(GpGraphics* graphics, GpUnit unit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "unit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetPageScale(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetPageScale(GpGraphics* graphics, REAL scale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "scale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetDpiX(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetDpiX(GpGraphics* graphics, REAL* dpi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetDpiY(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetDpiY(GpGraphics* graphics, REAL* dpi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTransformPoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTransformPoints(GpGraphics* graphics, GpCoordinateSpace destSpace, GpCoordinateSpace srcSpace, GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "destSpace", "srcSpace", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTransformPointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTransformPointsI(GpGraphics* graphics, GpCoordinateSpace destSpace, GpCoordinateSpace srcSpace, GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "destSpace", "srcSpace", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetNearestColor(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetNearestColor(GpGraphics* graphics, ARGB* argb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "argb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateHalftonePalette(jitter):
    """"
    [gdiplus.dll] HPALETTE GdipCreateHalftonePalette()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawLine(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawLine(GpGraphics* graphics, GpPen* pen, REAL x1, REAL y1, REAL x2, REAL y2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x1", "y1", "x2", "y2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawLineI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawLineI(GpGraphics* graphics, GpPen* pen, INT x1, INT y1, INT x2, INT y2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x1", "y1", "x2", "y2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawLines(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawLines(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawLinesI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawLinesI(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawArc(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawArc(GpGraphics* graphics, GpPen* pen, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawArcI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawArcI(GpGraphics* graphics, GpPen* pen, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawBezier(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawBezier(GpGraphics* graphics, GpPen* pen, REAL x1, REAL y1, REAL x2, REAL y2, REAL x3, REAL y3, REAL x4, REAL y4)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawBezierI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawBezierI(GpGraphics* graphics, GpPen* pen, INT x1, INT y1, INT x2, INT y2, INT x3, INT y3, INT x4, INT y4)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawBeziers(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawBeziers(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawBeziersI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawBeziersI(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawRectangle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawRectangle(GpGraphics* graphics, GpPen* pen, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawRectangleI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawRectangleI(GpGraphics* graphics, GpPen* pen, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawRectangles(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawRectangles(GpGraphics* graphics, GpPen* pen, GDIPCONST GpRectF* rects, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "rects", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawRectanglesI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawRectanglesI(GpGraphics* graphics, GpPen* pen, GDIPCONST GpRect* rects, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "rects", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawEllipse(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawEllipse(GpGraphics* graphics, GpPen* pen, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawEllipseI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawEllipseI(GpGraphics* graphics, GpPen* pen, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawPie(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawPie(GpGraphics* graphics, GpPen* pen, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawPieI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawPieI(GpGraphics* graphics, GpPen* pen, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawPolygon(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawPolygon(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawPolygonI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawPolygonI(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawPath(GpGraphics* graphics, GpPen* pen, GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCurve(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCurve(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCurveI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCurveI(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCurve2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCurve2(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCurve2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCurve2I(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCurve3(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCurve3(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count, INT offset, INT numberOfSegments, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count", "offset", "numberOfSegments", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCurve3I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCurve3I(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count, INT offset, INT numberOfSegments, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count", "offset", "numberOfSegments", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawClosedCurve(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawClosedCurve(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawClosedCurveI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawClosedCurveI(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawClosedCurve2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawClosedCurve2(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPointF* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawClosedCurve2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawClosedCurve2I(GpGraphics* graphics, GpPen* pen, GDIPCONST GpPoint* points, INT count, REAL tension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "pen", "points", "count", "tension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGraphicsClear(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGraphicsClear(GpGraphics* graphics, ARGB color)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "color"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillRectangle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillRectangle(GpGraphics* graphics, GpBrush* brush, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillRectangleI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillRectangleI(GpGraphics* graphics, GpBrush* brush, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillRectangles(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillRectangles(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpRectF* rects, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "rects", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillRectanglesI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillRectanglesI(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpRect* rects, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "rects", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPolygon(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPolygon(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPointF* points, INT count, GpFillMode fillMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count", "fillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPolygonI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPolygonI(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPoint* points, INT count, GpFillMode fillMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count", "fillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPolygon2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPolygon2(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPolygon2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPolygon2I(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillEllipse(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillEllipse(GpGraphics* graphics, GpBrush* brush, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillEllipseI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillEllipseI(GpGraphics* graphics, GpBrush* brush, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPie(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPie(GpGraphics* graphics, GpBrush* brush, REAL x, REAL y, REAL width, REAL height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPieI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPieI(GpGraphics* graphics, GpBrush* brush, INT x, INT y, INT width, INT height, REAL startAngle, REAL sweepAngle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "x", "y", "width", "height", "startAngle", "sweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillPath(GpGraphics* graphics, GpBrush* brush, GpPath* path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillClosedCurve(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillClosedCurve(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPointF* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillClosedCurveI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillClosedCurveI(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPoint* points, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillClosedCurve2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillClosedCurve2(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPointF* points, INT count, REAL tension, GpFillMode fillMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count", "tension", "fillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillClosedCurve2I(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillClosedCurve2I(GpGraphics* graphics, GpBrush* brush, GDIPCONST GpPoint* points, INT count, REAL tension, GpFillMode fillMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "points", "count", "tension", "fillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFillRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFillRegion(GpGraphics* graphics, GpBrush* brush, GpRegion* region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "brush", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImageFX(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImageFX(GpGraphics* graphics, GpImage* image, GpRectF* source, GpMatrix* xForm, CGpEffect* effect, GpImageAttributes* imageAttributes, GpUnit srcUnit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "source", "xForm", "effect", "imageAttributes", "srcUnit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImage(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImage(GpGraphics* graphics, GpImage* image, REAL x, REAL y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImageI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImageI(GpGraphics* graphics, GpImage* image, INT x, INT y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImageRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImageRect(GpGraphics* graphics, GpImage* image, REAL x, REAL y, REAL width, REAL height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImageRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImageRectI(GpGraphics* graphics, GpImage* image, INT x, INT y, INT width, INT height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "x", "y", "width", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImagePoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImagePoints(GpGraphics* graphics, GpImage* image, GDIPCONST GpPointF* dstpoints, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "dstpoints", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImagePointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImagePointsI(GpGraphics* graphics, GpImage* image, GDIPCONST GpPoint* dstpoints, INT count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "dstpoints", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImagePointRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImagePointRect(GpGraphics* graphics, GpImage* image, REAL x, REAL y, REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight, GpUnit srcUnit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "x", "y", "srcx", "srcy", "srcwidth", "srcheight", "srcUnit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImagePointRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImagePointRectI(GpGraphics* graphics, GpImage* image, INT x, INT y, INT srcx, INT srcy, INT srcwidth, INT srcheight, GpUnit srcUnit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "x", "y", "srcx", "srcy", "srcwidth", "srcheight", "srcUnit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImageRectRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImageRectRect(GpGraphics* graphics, GpImage* image, REAL dstx, REAL dsty, REAL dstwidth, REAL dstheight, REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight, GpUnit srcUnit, GDIPCONST GpImageAttributes* imageAttributes, DrawImageAbort callback, VOID* callbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "dstx", "dsty", "dstwidth", "dstheight", "srcx", "srcy", "srcwidth", "srcheight", "srcUnit", "imageAttributes", "callback", "callbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImageRectRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImageRectRectI(GpGraphics* graphics, GpImage* image, INT dstx, INT dsty, INT dstwidth, INT dstheight, INT srcx, INT srcy, INT srcwidth, INT srcheight, GpUnit srcUnit, GDIPCONST GpImageAttributes* imageAttributes, DrawImageAbort callback, VOID* callbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "dstx", "dsty", "dstwidth", "dstheight", "srcx", "srcy", "srcwidth", "srcheight", "srcUnit", "imageAttributes", "callback", "callbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImagePointsRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImagePointsRect(GpGraphics* graphics, GpImage* image, GDIPCONST GpPointF* points, INT count, REAL srcx, REAL srcy, REAL srcwidth, REAL srcheight, GpUnit srcUnit, GDIPCONST GpImageAttributes* imageAttributes, DrawImageAbort callback, VOID* callbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "points", "count", "srcx", "srcy", "srcwidth", "srcheight", "srcUnit", "imageAttributes", "callback", "callbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawImagePointsRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawImagePointsRectI(GpGraphics* graphics, GpImage* image, GDIPCONST GpPoint* points, INT count, INT srcx, INT srcy, INT srcwidth, INT srcheight, GpUnit srcUnit, GDIPCONST GpImageAttributes* imageAttributes, DrawImageAbort callback, VOID* callbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "image", "points", "count", "srcx", "srcy", "srcwidth", "srcheight", "srcUnit", "imageAttributes", "callback", "callbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileDestPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileDestPoint(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileDestPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileDestPointI(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileDestRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileDestRect(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileDestRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileDestRectI(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileDestPoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileDestPoints(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, GDIPCONST PointF* destPoints, INT count, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "destPoints", "count", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileDestPointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileDestPointsI(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, GDIPCONST Point* destPoints, INT count, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "destPoints", "count", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileSrcRectDestPoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileSrcRectDestPoint(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, Unit srcUnit, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "srcUnit", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileSrcRectDestPointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileSrcRectDestPointI(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, Unit srcUnit, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "srcUnit", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileSrcRectDestRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileSrcRectDestRect(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, Unit srcUnit, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "srcUnit", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileSrcRectDestRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileSrcRectDestRectI(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, Unit srcUnit, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "srcUnit", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileSrcRectDestPoints(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileSrcRectDestPoints(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, GDIPCONST PointF* destPoints, INT count, Unit srcUnit, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "destPoints", "count", "srcUnit", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEnumerateMetafileSrcRectDestPointsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEnumerateMetafileSrcRectDestPointsI(GpGraphics* graphics, GDIPCONST GpMetafile* metafile, GDIPCONST Point* destPoints, INT count, Unit srcUnit, EnumerateMetafileProc callback, VOID* callbackData, GDIPCONST GpImageAttributes* imageAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "metafile", "destPoints", "count", "srcUnit", "callback", "callbackData", "imageAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPlayMetafileRecord(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPlayMetafileRecord(GDIPCONST GpMetafile* metafile, EmfPlusRecordType recordType, UINT flags, UINT dataSize, GDIPCONST BYTE* data)
    """"
    ret_ad, args = jitter.func_args_stdcall(["metafile", "recordType", "flags", "dataSize", "data"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetClipGraphics(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetClipGraphics(GpGraphics* graphics, GpGraphics* srcgraphics, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "srcgraphics", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetClipRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetClipRect(GpGraphics* graphics, REAL x, REAL y, REAL width, REAL height, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y", "width", "height", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetClipRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetClipRectI(GpGraphics* graphics, INT x, INT y, INT width, INT height, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y", "width", "height", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetClipPath(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetClipPath(GpGraphics* graphics, GpPath* path, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "path", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetClipRegion(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetClipRegion(GpGraphics* graphics, GpRegion* region, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "region", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetClipHrgn(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetClipHrgn(GpGraphics* graphics, HRGN hRgn, CombineMode combineMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "hRgn", "combineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipResetClip(jitter):
    """"
    [gdiplus.dll] GpStatus GdipResetClip(GpGraphics* graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateClip(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateClip(GpGraphics* graphics, REAL dx, REAL dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTranslateClipI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTranslateClipI(GpGraphics* graphics, INT dx, INT dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetClip(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetClip(GpGraphics* graphics, GpRegion* region)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "region"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetClipBounds(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetClipBounds(GpGraphics* graphics, GpRectF* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetClipBoundsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetClipBoundsI(GpGraphics* graphics, GpRect* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsClipEmpty(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsClipEmpty(GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetVisibleClipBounds(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetVisibleClipBounds(GpGraphics* graphics, GpRectF* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetVisibleClipBoundsI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetVisibleClipBoundsI(GpGraphics* graphics, GpRect* rect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleClipEmpty(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleClipEmpty(GpGraphics* graphics, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisiblePoint(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisiblePoint(GpGraphics* graphics, REAL x, REAL y, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisiblePointI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisiblePointI(GpGraphics* graphics, INT x, INT y, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleRect(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleRect(GpGraphics* graphics, REAL x, REAL y, REAL width, REAL height, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y", "width", "height", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsVisibleRectI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsVisibleRectI(GpGraphics* graphics, INT x, INT y, INT width, INT height, BOOL* result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "x", "y", "width", "height", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSaveGraphics(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSaveGraphics(GpGraphics* graphics, GraphicsState* state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRestoreGraphics(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRestoreGraphics(GpGraphics* graphics, GraphicsState state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBeginContainer(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBeginContainer(GpGraphics* graphics, GDIPCONST GpRectF* dstrect, GDIPCONST GpRectF* srcrect, GpUnit unit, GraphicsContainer* state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dstrect", "srcrect", "unit", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBeginContainerI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBeginContainerI(GpGraphics* graphics, GDIPCONST GpRect* dstrect, GDIPCONST GpRect* srcrect, GpUnit unit, GraphicsContainer* state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "dstrect", "srcrect", "unit", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipBeginContainer2(jitter):
    """"
    [gdiplus.dll] GpStatus GdipBeginContainer2(GpGraphics* graphics, GraphicsContainer* state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEndContainer(jitter):
    """"
    [gdiplus.dll] GpStatus GdipEndContainer(GpGraphics* graphics, GraphicsContainer state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMetafileHeaderFromWmf(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMetafileHeaderFromWmf(HMETAFILE hWmf, GDIPCONST WmfPlaceableFileHeader* wmfPlaceableFileHeader, MetafileHeader* header)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWmf", "wmfPlaceableFileHeader", "header"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMetafileHeaderFromEmf(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMetafileHeaderFromEmf(HENHMETAFILE hEmf, MetafileHeader* header)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEmf", "header"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMetafileHeaderFromFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMetafileHeaderFromFile(GDIPCONST WCHAR* filename, MetafileHeader* header)
    """"
    ret_ad, args = jitter.func_args_stdcall(["filename", "header"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMetafileHeaderFromStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMetafileHeaderFromStream(IStream* stream, MetafileHeader* header)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "header"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMetafileHeaderFromMetafile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMetafileHeaderFromMetafile(GpMetafile* metafile, MetafileHeader* header)
    """"
    ret_ad, args = jitter.func_args_stdcall(["metafile", "header"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetHemfFromMetafile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetHemfFromMetafile(GpMetafile* metafile, HENHMETAFILE* hEmf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["metafile", "hEmf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateStreamOnFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateStreamOnFile(GDIPCONST WCHAR* filename, UINT access, IStream** stream)
    """"
    ret_ad, args = jitter.func_args_stdcall(["filename", "access", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMetafileFromWmf(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMetafileFromWmf(HMETAFILE hWmf, BOOL deleteWmf, GDIPCONST WmfPlaceableFileHeader* wmfPlaceableFileHeader, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWmf", "deleteWmf", "wmfPlaceableFileHeader", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMetafileFromEmf(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMetafileFromEmf(HENHMETAFILE hEmf, BOOL deleteEmf, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEmf", "deleteEmf", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMetafileFromFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMetafileFromFile(GDIPCONST WCHAR* file, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["file", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMetafileFromWmfFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMetafileFromWmfFile(GDIPCONST WCHAR* file, GDIPCONST WmfPlaceableFileHeader* wmfPlaceableFileHeader, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["file", "wmfPlaceableFileHeader", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateMetafileFromStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateMetafileFromStream(IStream* stream, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRecordMetafile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRecordMetafile(HDC referenceHdc, EmfType type, GDIPCONST GpRectF* frameRect, MetafileFrameUnit frameUnit, GDIPCONST WCHAR* description, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["referenceHdc", "type", "frameRect", "frameUnit", "description", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRecordMetafileI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRecordMetafileI(HDC referenceHdc, EmfType type, GDIPCONST GpRect* frameRect, MetafileFrameUnit frameUnit, GDIPCONST WCHAR* description, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["referenceHdc", "type", "frameRect", "frameUnit", "description", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRecordMetafileFileName(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRecordMetafileFileName(GDIPCONST WCHAR* fileName, HDC referenceHdc, EmfType type, GDIPCONST GpRectF* frameRect, MetafileFrameUnit frameUnit, GDIPCONST WCHAR* description, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fileName", "referenceHdc", "type", "frameRect", "frameUnit", "description", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRecordMetafileFileNameI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRecordMetafileFileNameI(GDIPCONST WCHAR* fileName, HDC referenceHdc, EmfType type, GDIPCONST GpRect* frameRect, MetafileFrameUnit frameUnit, GDIPCONST WCHAR* description, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fileName", "referenceHdc", "type", "frameRect", "frameUnit", "description", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRecordMetafileStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRecordMetafileStream(IStream* stream, HDC referenceHdc, EmfType type, GDIPCONST GpRectF* frameRect, MetafileFrameUnit frameUnit, GDIPCONST WCHAR* description, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "referenceHdc", "type", "frameRect", "frameUnit", "description", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipRecordMetafileStreamI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipRecordMetafileStreamI(IStream* stream, HDC referenceHdc, EmfType type, GDIPCONST GpRect* frameRect, MetafileFrameUnit frameUnit, GDIPCONST WCHAR* description, GpMetafile** metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["stream", "referenceHdc", "type", "frameRect", "frameUnit", "description", "metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetMetafileDownLevelRasterizationLimit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetMetafileDownLevelRasterizationLimit(GpMetafile* metafile, UINT metafileRasterizationLimitDpi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["metafile", "metafileRasterizationLimitDpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetMetafileDownLevelRasterizationLimit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetMetafileDownLevelRasterizationLimit(GDIPCONST GpMetafile* metafile, UINT* metafileRasterizationLimitDpi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["metafile", "metafileRasterizationLimitDpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageDecodersSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageDecodersSize(UINT* numDecoders, UINT* size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["numDecoders", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageDecoders(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageDecoders(UINT numDecoders, UINT size, ImageCodecInfo* decoders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["numDecoders", "size", "decoders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageEncodersSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageEncodersSize(UINT* numEncoders, UINT* size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["numEncoders", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetImageEncoders(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetImageEncoders(UINT numEncoders, UINT size, ImageCodecInfo* encoders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["numEncoders", "size", "encoders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipComment(jitter):
    """"
    [gdiplus.dll] GpStatus GdipComment(GpGraphics* graphics, UINT sizeData, GDIPCONST BYTE* data)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "sizeData", "data"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFontFamilyFromName(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFontFamilyFromName(GDIPCONST WCHAR* name, GpFontCollection* fontCollection, GpFontFamily** FontFamily)
    """"
    ret_ad, args = jitter.func_args_stdcall(["name", "fontCollection", "FontFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteFontFamily(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteFontFamily(GpFontFamily* FontFamily)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FontFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneFontFamily(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneFontFamily(GpFontFamily* FontFamily, GpFontFamily** clonedFontFamily)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FontFamily", "clonedFontFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetGenericFontFamilySansSerif(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetGenericFontFamilySansSerif(GpFontFamily** nativeFamily)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nativeFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetGenericFontFamilySerif(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetGenericFontFamilySerif(GpFontFamily** nativeFamily)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nativeFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetGenericFontFamilyMonospace(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetGenericFontFamilyMonospace(GpFontFamily** nativeFamily)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nativeFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFamilyName(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFamilyName(GDIPCONST GpFontFamily* family, LPWSTR name, LANGID language)
    """"
    ret_ad, args = jitter.func_args_stdcall(["family", "name", "language"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipIsStyleAvailable(jitter):
    """"
    [gdiplus.dll] GpStatus GdipIsStyleAvailable(GDIPCONST GpFontFamily* family, INT style, BOOL* IsStyleAvailable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["family", "style", "IsStyleAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFontCollectionEnumerable(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFontCollectionEnumerable(GpFontCollection* fontCollection, GpGraphics* graphics, INT* numFound)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection", "graphics", "numFound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipFontCollectionEnumerate(jitter):
    """"
    [gdiplus.dll] GpStatus GdipFontCollectionEnumerate(GpFontCollection* fontCollection, INT numSought, GpFontFamily* [] gpfamilies, INT* numFound, GpGraphics* graphics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection", "numSought", "gpfamilies", "numFound", "graphics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetEmHeight(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetEmHeight(GDIPCONST GpFontFamily* family, [FontStyle] style, UINT16* EmHeight)
    """"
    ret_ad, args = jitter.func_args_stdcall(["family", "style", "EmHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCellAscent(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCellAscent(GDIPCONST GpFontFamily* family, INT style, UINT16* CellAscent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["family", "style", "CellAscent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetCellDescent(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetCellDescent(GDIPCONST GpFontFamily* family, INT style, UINT16* CellDescent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["family", "style", "CellDescent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLineSpacing(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLineSpacing(GDIPCONST GpFontFamily* family, [FontStyle] style, UINT16* LineSpacing)
    """"
    ret_ad, args = jitter.func_args_stdcall(["family", "style", "LineSpacing"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFontFromDC(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFontFromDC(HDC hdc, GpFont** font)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "font"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFontFromLogfont(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFontFromLogfont(HDC hdc, GDIPCONST LOGFONT* logfont, GpFont** font)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "logfont", "font"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateFont(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateFont(GDIPCONST GpFontFamily* fontFamily, REAL emSize, [FontStyle] style, Unit unit, GpFont** font)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontFamily", "emSize", "style", "unit", "font"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneFont(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneFont(GpFont* font, GpFont** cloneFont)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "cloneFont"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteFont(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteFont(GpFont* font)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFamily(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFamily(GpFont* font, GpFontFamily** family)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "family"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontStyle(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontStyle(GpFont* font, [FontStyle*] style)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontSize(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontSize(GpFont* font, REAL* size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontUnit(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontUnit(GpFont* font, Unit* unit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "unit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontHeight(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontHeight(GDIPCONST GpFont* font, GDIPCONST GpGraphics* graphics, REAL* height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "graphics", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontHeightGivenDPI(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontHeightGivenDPI(GDIPCONST GpFont* font, REAL dpi, REAL* height)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "dpi", "height"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetLogFont(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetLogFont(GpFont* font, GpGraphics* graphics, LOGFONT* logfont)
    """"
    ret_ad, args = jitter.func_args_stdcall(["font", "graphics", "logfont"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipNewInstalledFontCollection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipNewInstalledFontCollection(GpFontCollection** fontCollection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipNewPrivateFontCollection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipNewPrivateFontCollection(GpFontCollection** fontCollection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeletePrivateFontCollection(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeletePrivateFontCollection(GpFontCollection** fontCollection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontCollectionFamilyCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontCollectionFamilyCount(GpFontCollection* fontCollection, INT* numFound)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection", "numFound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetFontCollectionFamilyList(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetFontCollectionFamilyList(GpFontCollection* fontCollection, INT numSought, GpFontFamily* [] gpfamilies, INT* numFound)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection", "numSought", "gpfamilies", "numFound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPrivateAddFontFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPrivateAddFontFile(GpFontCollection* fontCollection, GDIPCONST WCHAR* filename)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection", "filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipPrivateAddMemoryFont(jitter):
    """"
    [gdiplus.dll] GpStatus GdipPrivateAddMemoryFont(GpFontCollection* fontCollection, GDIPCONST void* memory, INT length)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fontCollection", "memory", "length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawString(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawString(GpGraphics* graphics, GDIPCONST WCHAR* string, INT length, GDIPCONST GpFont* font, GDIPCONST RectF* layoutRect, GDIPCONST GpStringFormat* stringFormat, GDIPCONST GpBrush* brush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "string", "length", "font", "layoutRect", "stringFormat", "brush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMeasureString(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMeasureString(GpGraphics* graphics, GDIPCONST WCHAR* string, INT length, GDIPCONST GpFont* font, GDIPCONST RectF* layoutRect, GDIPCONST GpStringFormat* stringFormat, RectF* boundingBox, INT* codepointsFitted, INT* linesFilled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "string", "length", "font", "layoutRect", "stringFormat", "boundingBox", "codepointsFitted", "linesFilled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMeasureCharacterRanges(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMeasureCharacterRanges(GpGraphics* graphics, GDIPCONST WCHAR* string, INT length, GDIPCONST GpFont* font, GDIPCONST GpStringFormat* stringFormat, INT regionCount, GpRegion** regions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "string", "length", "font", "stringFormat", "regionCount", "regions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawDriverString(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawDriverString(GpGraphics* graphics, GDIPCONST UINT16* text, INT length, GDIPCONST GpFont* font, GDIPCONST GpBrush* brush, GDIPCONST PointF* positions, [DriverStringOptions] flags, GDIPCONST GpMatrix* matrix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "text", "length", "font", "brush", "positions", "flags", "matrix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipMeasureDriverString(jitter):
    """"
    [gdiplus.dll] GpStatus GdipMeasureDriverString(GpGraphics* graphics, GDIPCONST UINT16* text, INT length, GDIPCONST GpFont* font, GDIPCONST PointF* positions, [DriverStringOptions] flags, GDIPCONST GpMatrix* matrix, RectF* boundingBox)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "text", "length", "font", "positions", "flags", "matrix", "boundingBox"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateStringFormat(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateStringFormat([StringFormatFlags] formatAttributes, LANGID language, GpStringFormat** format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["formatAttributes", "language", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipStringFormatGetGenericDefault(jitter):
    """"
    [gdiplus.dll] GpStatus GdipStringFormatGetGenericDefault(GpStringFormat** format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipStringFormatGetGenericTypographic(jitter):
    """"
    [gdiplus.dll] GpStatus GdipStringFormatGetGenericTypographic(GpStringFormat** format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteStringFormat(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteStringFormat(GpStringFormat* format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCloneStringFormat(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCloneStringFormat(GDIPCONST GpStringFormat* format, GpStringFormat** newFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "newFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatFlags(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatFlags(GpStringFormat* format, [StringFormatFlags] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatFlags(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatFlags(GDIPCONST GpStringFormat* format, [StringFormatFlags*] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatAlign(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatAlign(GpStringFormat* format, StringAlignment align)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "align"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatAlign(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatAlign(GDIPCONST GpStringFormat* format, StringAlignment* align)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "align"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatLineAlign(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatLineAlign(GpStringFormat* format, StringAlignment align)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "align"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatLineAlign(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatLineAlign(GDIPCONST GpStringFormat* format, StringAlignment* align)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "align"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatTrimming(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatTrimming(GpStringFormat* format, StringTrimming trimming)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "trimming"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatTrimming(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatTrimming(GDIPCONST GpStringFormat* format, StringTrimming* trimming)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "trimming"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatHotkeyPrefix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatHotkeyPrefix(GpStringFormat* format, [HotkeyPrefix] hotkeyPrefix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "hotkeyPrefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatHotkeyPrefix(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatHotkeyPrefix(GDIPCONST GpStringFormat* format, [HotkeyPrefix*] hotkeyPrefix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "hotkeyPrefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatTabStops(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatTabStops(GpStringFormat* format, REAL firstTabOffset, INT count, GDIPCONST REAL* tabStops)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "firstTabOffset", "count", "tabStops"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatTabStops(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatTabStops(GDIPCONST GpStringFormat* format, INT count, REAL* firstTabOffset, REAL* tabStops)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "count", "firstTabOffset", "tabStops"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatTabStopCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatTabStopCount(GDIPCONST GpStringFormat* format, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatDigitSubstitution(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatDigitSubstitution(GpStringFormat* format, LANGID language, StringDigitSubstitute substitute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "language", "substitute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatDigitSubstitution(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatDigitSubstitution(GDIPCONST GpStringFormat* format, LANGID* language, StringDigitSubstitute* substitute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "language", "substitute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipGetStringFormatMeasurableCharacterRangeCount(jitter):
    """"
    [gdiplus.dll] GpStatus GdipGetStringFormatMeasurableCharacterRangeCount(GDIPCONST GpStringFormat* format, INT* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetStringFormatMeasurableCharacterRanges(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetStringFormatMeasurableCharacterRanges(GpStringFormat* format, INT rangeCount, GDIPCONST CharacterRange* ranges)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "rangeCount", "ranges"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipCreateCachedBitmap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipCreateCachedBitmap(GpBitmap* bitmap, GpGraphics* graphics, GpCachedBitmap** cachedBitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bitmap", "graphics", "cachedBitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDeleteCachedBitmap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDeleteCachedBitmap(GpCachedBitmap* cachedBitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cachedBitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipDrawCachedBitmap(jitter):
    """"
    [gdiplus.dll] GpStatus GdipDrawCachedBitmap(GpGraphics* graphics, GpCachedBitmap* cachedBitmap, INT x, INT y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["graphics", "cachedBitmap", "x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipEmfToWmfBits(jitter):
    """"
    [gdiplus.dll] UINT GdipEmfToWmfBits(HENHMETAFILE hemf, UINT cbData16, LPBYTE pData16, INT iMapMode, INT eFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cbData16", "pData16", "iMapMode", "eFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipSetImageAttributesCachedBackground(jitter):
    """"
    [gdiplus.dll] GpStatus GdipSetImageAttributesCachedBackground(GpImageAttributes* imageattr, BOOL enableFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["imageattr", "enableFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipTestControl(jitter):
    """"
    [gdiplus.dll] GpStatus GdipTestControl(GpTestControlEnum control, void* param)
    """"
    ret_ad, args = jitter.func_args_stdcall(["control", "param"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdiplusNotificationHook(jitter):
    """"
    [gdiplus.dll] GpStatus GdiplusNotificationHook(ULONG_PTR* token)
    """"
    ret_ad, args = jitter.func_args_stdcall(["token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdiplusNotificationUnhook(jitter):
    """"
    [gdiplus.dll] VOID GdiplusNotificationUnhook(ULONG_PTR token)
    """"
    ret_ad, args = jitter.func_args_stdcall(["token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipConvertToEmfPlus(jitter):
    """"
    [gdiplus.dll] GpStatus GdipConvertToEmfPlus(const GpGraphics* refGraphics, GpMetafile* metafile, INT* conversionFailureFlag, EmfType emfType, const WCHAR* description, GpMetafile** out_metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["refGraphics", "metafile", "conversionFailureFlag", "emfType", "description", "out_metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipConvertToEmfPlusToFile(jitter):
    """"
    [gdiplus.dll] GpStatus GdipConvertToEmfPlusToFile(const GpGraphics* refGraphics, GpMetafile* metafile, INT* conversionFailureFlag, const WCHAR* filename, EmfType emfType, const WCHAR* description, GpMetafile** out_metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["refGraphics", "metafile", "conversionFailureFlag", "filename", "emfType", "description", "out_metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdiplus_GdipConvertToEmfPlusToStream(jitter):
    """"
    [gdiplus.dll] GpStatus GdipConvertToEmfPlusToStream(const GpGraphics* refGraphics, GpMetafile* metafile, INT* conversionFailureFlag, IStream* stream, EmfType emfType, const WCHAR* description, GpMetafile** out_metafile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["refGraphics", "metafile", "conversionFailureFlag", "stream", "emfType", "description", "out_metafile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
