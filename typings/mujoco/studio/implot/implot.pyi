from __future__ import annotations
import collections.abc
import mujoco.studio.dear_imgui.dear_imgui
import typing
__all__: list[str] = ['Annotation', 'Axis', 'AxisFlags', 'BarGroupsFlags', 'BarsFlags', 'BeginAlignedPlots', 'BeginDragDropSourceAxis', 'BeginDragDropSourceItem', 'BeginDragDropSourcePlot', 'BeginDragDropTargetAxis', 'BeginDragDropTargetLegend', 'BeginDragDropTargetPlot', 'BeginLegendPopup', 'BeginPlot', 'BeginSubplots', 'CancelPlotSelection', 'Col', 'ColormapScaleFlags', 'Cond', 'CreateContext', 'DestroyContext', 'DigitalFlags', 'DragLineX', 'DragLineY', 'DragPoint', 'DragRect', 'DragToolFlags', 'DummyFlags', 'EndAlignedPlots', 'EndDragDropSource', 'EndDragDropTarget', 'EndLegendPopup', 'EndPlot', 'EndSubplots', 'ErrorBarsFlags', 'Flags', 'GetPlotLimits', 'GetPlotMousePos', 'GetPlotPos', 'GetPlotSelection', 'GetPlotSize', 'HeatmapFlags', 'HideNextItem', 'HistogramFlags', 'ImageFlags', 'InfLinesFlags', 'IsAxisHovered', 'IsLegendEntryHovered', 'IsPlotHovered', 'IsPlotSelected', 'IsSubplotsHovered', 'ItemFlags', 'LegendFlags', 'LineFlags', 'Location', 'Marker', 'MouseTextFlags', 'PieChartFlags', 'PixelsToPlot', 'PlotBars', 'PlotDigital', 'PlotDummy', 'PlotErrorBars', 'PlotImage', 'PlotLine', 'PlotScatter', 'PlotShaded', 'PlotStairs', 'PlotStems', 'PlotText', 'PlotToPixels', 'Point', 'PopPlotClipRect', 'PopStyleColor', 'PopStyleVar', 'PushPlotClipRect', 'PushStyleColor', 'PushStyleVar', 'Range', 'Scale', 'ScatterFlags', 'SetAxes', 'SetAxis', 'SetNextAxesLimits', 'SetNextAxesToFit', 'SetNextAxisLimits', 'SetNextAxisLinks', 'SetNextAxisToFit', 'SetupAxes', 'SetupAxesLimits', 'SetupAxis', 'SetupAxisFormat', 'SetupAxisLimits', 'SetupAxisLimitsConstraints', 'SetupAxisLinks', 'SetupAxisScale', 'SetupAxisTicks', 'SetupAxisZoomConstraints', 'SetupFinish', 'SetupLegend', 'SetupMouseText', 'ShadedFlags', 'StairsFlags', 'StemsFlags', 'StyleVar', 'SubplotFlags', 'TagX', 'TagY', 'TextFlags', 'set_imgui_context', 'set_implot_context']
class Axis:
    """
    Members:
    
      X1
    
      X2
    
      X3
    
      Y1
    
      Y2
    
      Y3
    """
    X1: typing.ClassVar[Axis]  # value = <Axis.X1: 0>
    X2: typing.ClassVar[Axis]  # value = <Axis.X2: 1>
    X3: typing.ClassVar[Axis]  # value = <Axis.X3: 2>
    Y1: typing.ClassVar[Axis]  # value = <Axis.Y1: 3>
    Y2: typing.ClassVar[Axis]  # value = <Axis.Y2: 4>
    Y3: typing.ClassVar[Axis]  # value = <Axis.Y3: 5>
    __members__: typing.ClassVar[dict[str, Axis]]  # value = {'X1': <Axis.X1: 0>, 'X2': <Axis.X2: 1>, 'X3': <Axis.X3: 2>, 'Y1': <Axis.Y1: 3>, 'Y2': <Axis.Y2: 4>, 'Y3': <Axis.Y3: 5>}
    @typing.overload
    def __eq__(self, other: Axis) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Axis) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AxisFlags:
    """
    Members:
    
      None
    
      NoLabel
    
      NoGridLines
    
      NoTickMarks
    
      NoTickLabels
    
      NoInitialFit
    
      NoMenus
    
      NoSideSwitch
    
      NoHighlight
    
      Opposite
    
      Foreground
    
      Invert
    
      AutoFit
    
      RangeFit
    
      PanStretch
    
      LockMin
    
      LockMax
    
      Lock
    
      NoDecorations
    
      AuxDefault
    """
    AutoFit: typing.ClassVar[AxisFlags]  # value = <AxisFlags.AutoFit: 2048>
    AuxDefault: typing.ClassVar[AxisFlags]  # value = <AxisFlags.AuxDefault: 258>
    Foreground: typing.ClassVar[AxisFlags]  # value = <AxisFlags.Foreground: 512>
    Invert: typing.ClassVar[AxisFlags]  # value = <AxisFlags.Invert: 1024>
    Lock: typing.ClassVar[AxisFlags]  # value = <AxisFlags.Lock: 49152>
    LockMax: typing.ClassVar[AxisFlags]  # value = <AxisFlags.LockMax: 32768>
    LockMin: typing.ClassVar[AxisFlags]  # value = <AxisFlags.LockMin: 16384>
    NoDecorations: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoDecorations: 15>
    NoGridLines: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoGridLines: 2>
    NoHighlight: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoHighlight: 128>
    NoInitialFit: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoInitialFit: 16>
    NoLabel: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoLabel: 1>
    NoMenus: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoMenus: 32>
    NoSideSwitch: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoSideSwitch: 64>
    NoTickLabels: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoTickLabels: 8>
    NoTickMarks: typing.ClassVar[AxisFlags]  # value = <AxisFlags.NoTickMarks: 4>
    None: typing.ClassVar[AxisFlags]  # value = <AxisFlags.None: 0>
    Opposite: typing.ClassVar[AxisFlags]  # value = <AxisFlags.Opposite: 256>
    PanStretch: typing.ClassVar[AxisFlags]  # value = <AxisFlags.PanStretch: 8192>
    RangeFit: typing.ClassVar[AxisFlags]  # value = <AxisFlags.RangeFit: 4096>
    __members__: typing.ClassVar[dict[str, AxisFlags]]  # value = {'None': <AxisFlags.None: 0>, 'NoLabel': <AxisFlags.NoLabel: 1>, 'NoGridLines': <AxisFlags.NoGridLines: 2>, 'NoTickMarks': <AxisFlags.NoTickMarks: 4>, 'NoTickLabels': <AxisFlags.NoTickLabels: 8>, 'NoInitialFit': <AxisFlags.NoInitialFit: 16>, 'NoMenus': <AxisFlags.NoMenus: 32>, 'NoSideSwitch': <AxisFlags.NoSideSwitch: 64>, 'NoHighlight': <AxisFlags.NoHighlight: 128>, 'Opposite': <AxisFlags.Opposite: 256>, 'Foreground': <AxisFlags.Foreground: 512>, 'Invert': <AxisFlags.Invert: 1024>, 'AutoFit': <AxisFlags.AutoFit: 2048>, 'RangeFit': <AxisFlags.RangeFit: 4096>, 'PanStretch': <AxisFlags.PanStretch: 8192>, 'LockMin': <AxisFlags.LockMin: 16384>, 'LockMax': <AxisFlags.LockMax: 32768>, 'Lock': <AxisFlags.Lock: 49152>, 'NoDecorations': <AxisFlags.NoDecorations: 15>, 'AuxDefault': <AxisFlags.AuxDefault: 258>}
    @typing.overload
    def __eq__(self, other: AxisFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: AxisFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BarGroupsFlags:
    """
    Members:
    
      None
    
      Horizontal
    
      Stacked
    """
    Horizontal: typing.ClassVar[BarGroupsFlags]  # value = <BarGroupsFlags.Horizontal: 1024>
    None: typing.ClassVar[BarGroupsFlags]  # value = <BarGroupsFlags.None: 0>
    Stacked: typing.ClassVar[BarGroupsFlags]  # value = <BarGroupsFlags.Stacked: 2048>
    __members__: typing.ClassVar[dict[str, BarGroupsFlags]]  # value = {'None': <BarGroupsFlags.None: 0>, 'Horizontal': <BarGroupsFlags.Horizontal: 1024>, 'Stacked': <BarGroupsFlags.Stacked: 2048>}
    @typing.overload
    def __eq__(self, other: BarGroupsFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: BarGroupsFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BarsFlags:
    """
    Members:
    
      None
    
      Horizontal
    """
    Horizontal: typing.ClassVar[BarsFlags]  # value = <BarsFlags.Horizontal: 1024>
    None: typing.ClassVar[BarsFlags]  # value = <BarsFlags.None: 0>
    __members__: typing.ClassVar[dict[str, BarsFlags]]  # value = {'None': <BarsFlags.None: 0>, 'Horizontal': <BarsFlags.Horizontal: 1024>}
    @typing.overload
    def __eq__(self, other: BarsFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: BarsFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Col:
    """
    Members:
    
      FrameBg
    
      PlotBg
    
      PlotBorder
    
      LegendBg
    
      LegendBorder
    
      LegendText
    
      TitleText
    
      InlayText
    
      AxisText
    
      AxisGrid
    
      AxisTick
    
      AxisBg
    
      AxisBgHovered
    
      AxisBgActive
    
      Selection
    
      Crosshairs
    """
    AxisBg: typing.ClassVar[Col]  # value = <Col.AxisBg: 11>
    AxisBgActive: typing.ClassVar[Col]  # value = <Col.AxisBgActive: 13>
    AxisBgHovered: typing.ClassVar[Col]  # value = <Col.AxisBgHovered: 12>
    AxisGrid: typing.ClassVar[Col]  # value = <Col.AxisGrid: 9>
    AxisText: typing.ClassVar[Col]  # value = <Col.AxisText: 8>
    AxisTick: typing.ClassVar[Col]  # value = <Col.AxisTick: 10>
    Crosshairs: typing.ClassVar[Col]  # value = <Col.Crosshairs: 15>
    FrameBg: typing.ClassVar[Col]  # value = <Col.FrameBg: 0>
    InlayText: typing.ClassVar[Col]  # value = <Col.InlayText: 7>
    LegendBg: typing.ClassVar[Col]  # value = <Col.LegendBg: 3>
    LegendBorder: typing.ClassVar[Col]  # value = <Col.LegendBorder: 4>
    LegendText: typing.ClassVar[Col]  # value = <Col.LegendText: 5>
    PlotBg: typing.ClassVar[Col]  # value = <Col.PlotBg: 1>
    PlotBorder: typing.ClassVar[Col]  # value = <Col.PlotBorder: 2>
    Selection: typing.ClassVar[Col]  # value = <Col.Selection: 14>
    TitleText: typing.ClassVar[Col]  # value = <Col.TitleText: 6>
    __members__: typing.ClassVar[dict[str, Col]]  # value = {'FrameBg': <Col.FrameBg: 0>, 'PlotBg': <Col.PlotBg: 1>, 'PlotBorder': <Col.PlotBorder: 2>, 'LegendBg': <Col.LegendBg: 3>, 'LegendBorder': <Col.LegendBorder: 4>, 'LegendText': <Col.LegendText: 5>, 'TitleText': <Col.TitleText: 6>, 'InlayText': <Col.InlayText: 7>, 'AxisText': <Col.AxisText: 8>, 'AxisGrid': <Col.AxisGrid: 9>, 'AxisTick': <Col.AxisTick: 10>, 'AxisBg': <Col.AxisBg: 11>, 'AxisBgHovered': <Col.AxisBgHovered: 12>, 'AxisBgActive': <Col.AxisBgActive: 13>, 'Selection': <Col.Selection: 14>, 'Crosshairs': <Col.Crosshairs: 15>}
    @typing.overload
    def __eq__(self, other: Col) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Col) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ColormapScaleFlags:
    """
    Members:
    
      None
    
      NoLabel
    
      Opposite
    
      Invert
    """
    Invert: typing.ClassVar[ColormapScaleFlags]  # value = <ColormapScaleFlags.Invert: 4>
    NoLabel: typing.ClassVar[ColormapScaleFlags]  # value = <ColormapScaleFlags.NoLabel: 1>
    None: typing.ClassVar[ColormapScaleFlags]  # value = <ColormapScaleFlags.None: 0>
    Opposite: typing.ClassVar[ColormapScaleFlags]  # value = <ColormapScaleFlags.Opposite: 2>
    __members__: typing.ClassVar[dict[str, ColormapScaleFlags]]  # value = {'None': <ColormapScaleFlags.None: 0>, 'NoLabel': <ColormapScaleFlags.NoLabel: 1>, 'Opposite': <ColormapScaleFlags.Opposite: 2>, 'Invert': <ColormapScaleFlags.Invert: 4>}
    @typing.overload
    def __eq__(self, other: ColormapScaleFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: ColormapScaleFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Cond:
    """
    Members:
    
      None
    
      Always
    
      Once
    """
    Always: typing.ClassVar[Cond]  # value = <Cond.Always: 1>
    None: typing.ClassVar[Cond]  # value = <Cond.None: 0>
    Once: typing.ClassVar[Cond]  # value = <Cond.Once: 2>
    __members__: typing.ClassVar[dict[str, Cond]]  # value = {'None': <Cond.None: 0>, 'Always': <Cond.Always: 1>, 'Once': <Cond.Once: 2>}
    @typing.overload
    def __eq__(self, other: Cond) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Cond) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DigitalFlags:
    """
    Members:
    
      ImPlotNone
    """
    ImPlotNone: typing.ClassVar[DigitalFlags]  # value = <DigitalFlags.ImPlotNone: 0>
    __members__: typing.ClassVar[dict[str, DigitalFlags]]  # value = {'ImPlotNone': <DigitalFlags.ImPlotNone: 0>}
    @typing.overload
    def __eq__(self, other: DigitalFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: DigitalFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DragToolFlags:
    """
    Members:
    
      None
    
      NoCursors
    
      NoFit
    
      NoInputs
    
      Delayed
    """
    Delayed: typing.ClassVar[DragToolFlags]  # value = <DragToolFlags.Delayed: 8>
    NoCursors: typing.ClassVar[DragToolFlags]  # value = <DragToolFlags.NoCursors: 1>
    NoFit: typing.ClassVar[DragToolFlags]  # value = <DragToolFlags.NoFit: 2>
    NoInputs: typing.ClassVar[DragToolFlags]  # value = <DragToolFlags.NoInputs: 4>
    None: typing.ClassVar[DragToolFlags]  # value = <DragToolFlags.None: 0>
    __members__: typing.ClassVar[dict[str, DragToolFlags]]  # value = {'None': <DragToolFlags.None: 0>, 'NoCursors': <DragToolFlags.NoCursors: 1>, 'NoFit': <DragToolFlags.NoFit: 2>, 'NoInputs': <DragToolFlags.NoInputs: 4>, 'Delayed': <DragToolFlags.Delayed: 8>}
    @typing.overload
    def __eq__(self, other: DragToolFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: DragToolFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DummyFlags:
    """
    Members:
    
      None
    """
    None: typing.ClassVar[DummyFlags]  # value = <DummyFlags.None: 0>
    __members__: typing.ClassVar[dict[str, DummyFlags]]  # value = {'None': <DummyFlags.None: 0>}
    @typing.overload
    def __eq__(self, other: DummyFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: DummyFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ErrorBarsFlags:
    """
    Members:
    
      None
    
      Horizontal
    """
    Horizontal: typing.ClassVar[ErrorBarsFlags]  # value = <ErrorBarsFlags.Horizontal: 1024>
    None: typing.ClassVar[ErrorBarsFlags]  # value = <ErrorBarsFlags.None: 0>
    __members__: typing.ClassVar[dict[str, ErrorBarsFlags]]  # value = {'None': <ErrorBarsFlags.None: 0>, 'Horizontal': <ErrorBarsFlags.Horizontal: 1024>}
    @typing.overload
    def __eq__(self, other: ErrorBarsFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: ErrorBarsFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Flags:
    """
    Members:
    
      None
    
      NoTitle
    
      NoLegend
    
      NoMouseText
    
      NoInputs
    
      NoMenus
    
      NoBoxSelect
    
      NoFrame
    
      Equal
    
      Crosshairs
    
      CanvasOnly
    """
    CanvasOnly: typing.ClassVar[Flags]  # value = <Flags.CanvasOnly: 55>
    Crosshairs: typing.ClassVar[Flags]  # value = <Flags.Crosshairs: 256>
    Equal: typing.ClassVar[Flags]  # value = <Flags.Equal: 128>
    NoBoxSelect: typing.ClassVar[Flags]  # value = <Flags.NoBoxSelect: 32>
    NoFrame: typing.ClassVar[Flags]  # value = <Flags.NoFrame: 64>
    NoInputs: typing.ClassVar[Flags]  # value = <Flags.NoInputs: 8>
    NoLegend: typing.ClassVar[Flags]  # value = <Flags.NoLegend: 2>
    NoMenus: typing.ClassVar[Flags]  # value = <Flags.NoMenus: 16>
    NoMouseText: typing.ClassVar[Flags]  # value = <Flags.NoMouseText: 4>
    NoTitle: typing.ClassVar[Flags]  # value = <Flags.NoTitle: 1>
    None: typing.ClassVar[Flags]  # value = <Flags.None: 0>
    __members__: typing.ClassVar[dict[str, Flags]]  # value = {'None': <Flags.None: 0>, 'NoTitle': <Flags.NoTitle: 1>, 'NoLegend': <Flags.NoLegend: 2>, 'NoMouseText': <Flags.NoMouseText: 4>, 'NoInputs': <Flags.NoInputs: 8>, 'NoMenus': <Flags.NoMenus: 16>, 'NoBoxSelect': <Flags.NoBoxSelect: 32>, 'NoFrame': <Flags.NoFrame: 64>, 'Equal': <Flags.Equal: 128>, 'Crosshairs': <Flags.Crosshairs: 256>, 'CanvasOnly': <Flags.CanvasOnly: 55>}
    @typing.overload
    def __eq__(self, other: Flags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Flags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class HeatmapFlags:
    """
    Members:
    
      None
    
      ColMajor
    """
    ColMajor: typing.ClassVar[HeatmapFlags]  # value = <HeatmapFlags.ColMajor: 1024>
    None: typing.ClassVar[HeatmapFlags]  # value = <HeatmapFlags.None: 0>
    __members__: typing.ClassVar[dict[str, HeatmapFlags]]  # value = {'None': <HeatmapFlags.None: 0>, 'ColMajor': <HeatmapFlags.ColMajor: 1024>}
    @typing.overload
    def __eq__(self, other: HeatmapFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: HeatmapFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class HistogramFlags:
    """
    Members:
    
      None
    
      Horizontal
    
      Cumulative
    
      Density
    
      NoOutliers
    
      ColMajor
    """
    ColMajor: typing.ClassVar[HistogramFlags]  # value = <HistogramFlags.ColMajor: 16384>
    Cumulative: typing.ClassVar[HistogramFlags]  # value = <HistogramFlags.Cumulative: 2048>
    Density: typing.ClassVar[HistogramFlags]  # value = <HistogramFlags.Density: 4096>
    Horizontal: typing.ClassVar[HistogramFlags]  # value = <HistogramFlags.Horizontal: 1024>
    NoOutliers: typing.ClassVar[HistogramFlags]  # value = <HistogramFlags.NoOutliers: 8192>
    None: typing.ClassVar[HistogramFlags]  # value = <HistogramFlags.None: 0>
    __members__: typing.ClassVar[dict[str, HistogramFlags]]  # value = {'None': <HistogramFlags.None: 0>, 'Horizontal': <HistogramFlags.Horizontal: 1024>, 'Cumulative': <HistogramFlags.Cumulative: 2048>, 'Density': <HistogramFlags.Density: 4096>, 'NoOutliers': <HistogramFlags.NoOutliers: 8192>, 'ColMajor': <HistogramFlags.ColMajor: 16384>}
    @typing.overload
    def __eq__(self, other: HistogramFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: HistogramFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ImageFlags:
    """
    Members:
    
      None
    """
    None: typing.ClassVar[ImageFlags]  # value = <ImageFlags.None: 0>
    __members__: typing.ClassVar[dict[str, ImageFlags]]  # value = {'None': <ImageFlags.None: 0>}
    @typing.overload
    def __eq__(self, other: ImageFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: ImageFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class InfLinesFlags:
    """
    Members:
    
      None
    
      Horizontal
    """
    Horizontal: typing.ClassVar[InfLinesFlags]  # value = <InfLinesFlags.Horizontal: 1024>
    None: typing.ClassVar[InfLinesFlags]  # value = <InfLinesFlags.None: 0>
    __members__: typing.ClassVar[dict[str, InfLinesFlags]]  # value = {'None': <InfLinesFlags.None: 0>, 'Horizontal': <InfLinesFlags.Horizontal: 1024>}
    @typing.overload
    def __eq__(self, other: InfLinesFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: InfLinesFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ItemFlags:
    """
    Members:
    
      None
    
      NoLegend
    
      NoFit
    """
    NoFit: typing.ClassVar[ItemFlags]  # value = <ItemFlags.NoFit: 2>
    NoLegend: typing.ClassVar[ItemFlags]  # value = <ItemFlags.NoLegend: 1>
    None: typing.ClassVar[ItemFlags]  # value = <ItemFlags.None: 0>
    __members__: typing.ClassVar[dict[str, ItemFlags]]  # value = {'None': <ItemFlags.None: 0>, 'NoLegend': <ItemFlags.NoLegend: 1>, 'NoFit': <ItemFlags.NoFit: 2>}
    @typing.overload
    def __eq__(self, other: ItemFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: ItemFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LegendFlags:
    """
    Members:
    
      None
    
      NoButtons
    
      NoHighlightItem
    
      NoHighlightAxis
    
      NoMenus
    
      Outside
    
      Horizontal
    
      Sort
    
      Reverse
    """
    Horizontal: typing.ClassVar[LegendFlags]  # value = <LegendFlags.Horizontal: 32>
    NoButtons: typing.ClassVar[LegendFlags]  # value = <LegendFlags.NoButtons: 1>
    NoHighlightAxis: typing.ClassVar[LegendFlags]  # value = <LegendFlags.NoHighlightAxis: 4>
    NoHighlightItem: typing.ClassVar[LegendFlags]  # value = <LegendFlags.NoHighlightItem: 2>
    NoMenus: typing.ClassVar[LegendFlags]  # value = <LegendFlags.NoMenus: 8>
    None: typing.ClassVar[LegendFlags]  # value = <LegendFlags.None: 0>
    Outside: typing.ClassVar[LegendFlags]  # value = <LegendFlags.Outside: 16>
    Reverse: typing.ClassVar[LegendFlags]  # value = <LegendFlags.Reverse: 128>
    Sort: typing.ClassVar[LegendFlags]  # value = <LegendFlags.Sort: 64>
    __members__: typing.ClassVar[dict[str, LegendFlags]]  # value = {'None': <LegendFlags.None: 0>, 'NoButtons': <LegendFlags.NoButtons: 1>, 'NoHighlightItem': <LegendFlags.NoHighlightItem: 2>, 'NoHighlightAxis': <LegendFlags.NoHighlightAxis: 4>, 'NoMenus': <LegendFlags.NoMenus: 8>, 'Outside': <LegendFlags.Outside: 16>, 'Horizontal': <LegendFlags.Horizontal: 32>, 'Sort': <LegendFlags.Sort: 64>, 'Reverse': <LegendFlags.Reverse: 128>}
    @typing.overload
    def __eq__(self, other: LegendFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: LegendFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LineFlags:
    """
    Members:
    
      None
    
      Segments
    
      Loop
    
      SkipNaN
    
      NoClip
    
      Shaded
    """
    Loop: typing.ClassVar[LineFlags]  # value = <LineFlags.Loop: 2048>
    NoClip: typing.ClassVar[LineFlags]  # value = <LineFlags.NoClip: 8192>
    None: typing.ClassVar[LineFlags]  # value = <LineFlags.None: 0>
    Segments: typing.ClassVar[LineFlags]  # value = <LineFlags.Segments: 1024>
    Shaded: typing.ClassVar[LineFlags]  # value = <LineFlags.Shaded: 16384>
    SkipNaN: typing.ClassVar[LineFlags]  # value = <LineFlags.SkipNaN: 4096>
    __members__: typing.ClassVar[dict[str, LineFlags]]  # value = {'None': <LineFlags.None: 0>, 'Segments': <LineFlags.Segments: 1024>, 'Loop': <LineFlags.Loop: 2048>, 'SkipNaN': <LineFlags.SkipNaN: 4096>, 'NoClip': <LineFlags.NoClip: 8192>, 'Shaded': <LineFlags.Shaded: 16384>}
    @typing.overload
    def __eq__(self, other: LineFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: LineFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Location:
    """
    Members:
    
      Center
    
      North
    
      South
    
      West
    
      East
    
      NorthWest
    
      NorthEast
    
      SouthWest
    
      SouthEast
    """
    Center: typing.ClassVar[Location]  # value = <Location.Center: 0>
    East: typing.ClassVar[Location]  # value = <Location.East: 8>
    North: typing.ClassVar[Location]  # value = <Location.North: 1>
    NorthEast: typing.ClassVar[Location]  # value = <Location.NorthEast: 9>
    NorthWest: typing.ClassVar[Location]  # value = <Location.NorthWest: 5>
    South: typing.ClassVar[Location]  # value = <Location.South: 2>
    SouthEast: typing.ClassVar[Location]  # value = <Location.SouthEast: 10>
    SouthWest: typing.ClassVar[Location]  # value = <Location.SouthWest: 6>
    West: typing.ClassVar[Location]  # value = <Location.West: 4>
    __members__: typing.ClassVar[dict[str, Location]]  # value = {'Center': <Location.Center: 0>, 'North': <Location.North: 1>, 'South': <Location.South: 2>, 'West': <Location.West: 4>, 'East': <Location.East: 8>, 'NorthWest': <Location.NorthWest: 5>, 'NorthEast': <Location.NorthEast: 9>, 'SouthWest': <Location.SouthWest: 6>, 'SouthEast': <Location.SouthEast: 10>}
    @typing.overload
    def __eq__(self, other: Location) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Location) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Marker:
    """
    Members:
    
      None
    
      Circle
    
      Square
    
      Diamond
    
      Up
    
      Down
    
      Left
    
      Right
    
      Cross
    
      Plus
    
      Asterisk
    """
    Asterisk: typing.ClassVar[Marker]  # value = <Marker.Asterisk: 9>
    Circle: typing.ClassVar[Marker]  # value = <Marker.Circle: 0>
    Cross: typing.ClassVar[Marker]  # value = <Marker.Cross: 7>
    Diamond: typing.ClassVar[Marker]  # value = <Marker.Diamond: 2>
    Down: typing.ClassVar[Marker]  # value = <Marker.Down: 4>
    Left: typing.ClassVar[Marker]  # value = <Marker.Left: 5>
    None: typing.ClassVar[Marker]  # value = <Marker.None: -2>
    Plus: typing.ClassVar[Marker]  # value = <Marker.Plus: 8>
    Right: typing.ClassVar[Marker]  # value = <Marker.Right: 6>
    Square: typing.ClassVar[Marker]  # value = <Marker.Square: 1>
    Up: typing.ClassVar[Marker]  # value = <Marker.Up: 3>
    __members__: typing.ClassVar[dict[str, Marker]]  # value = {'None': <Marker.None: -2>, 'Circle': <Marker.Circle: 0>, 'Square': <Marker.Square: 1>, 'Diamond': <Marker.Diamond: 2>, 'Up': <Marker.Up: 3>, 'Down': <Marker.Down: 4>, 'Left': <Marker.Left: 5>, 'Right': <Marker.Right: 6>, 'Cross': <Marker.Cross: 7>, 'Plus': <Marker.Plus: 8>, 'Asterisk': <Marker.Asterisk: 9>}
    @typing.overload
    def __eq__(self, other: Marker) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Marker) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MouseTextFlags:
    """
    Members:
    
      None
    
      NoAuxAxes
    
      NoFormat
    
      ShowAlways
    """
    NoAuxAxes: typing.ClassVar[MouseTextFlags]  # value = <MouseTextFlags.NoAuxAxes: 1>
    NoFormat: typing.ClassVar[MouseTextFlags]  # value = <MouseTextFlags.NoFormat: 2>
    None: typing.ClassVar[MouseTextFlags]  # value = <MouseTextFlags.None: 0>
    ShowAlways: typing.ClassVar[MouseTextFlags]  # value = <MouseTextFlags.ShowAlways: 4>
    __members__: typing.ClassVar[dict[str, MouseTextFlags]]  # value = {'None': <MouseTextFlags.None: 0>, 'NoAuxAxes': <MouseTextFlags.NoAuxAxes: 1>, 'NoFormat': <MouseTextFlags.NoFormat: 2>, 'ShowAlways': <MouseTextFlags.ShowAlways: 4>}
    @typing.overload
    def __eq__(self, other: MouseTextFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: MouseTextFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PieChartFlags:
    """
    Members:
    
      None
    
      Normalize
    
      IgnoreHidden
    
      Exploding
    """
    Exploding: typing.ClassVar[PieChartFlags]  # value = <PieChartFlags.Exploding: 4096>
    IgnoreHidden: typing.ClassVar[PieChartFlags]  # value = <PieChartFlags.IgnoreHidden: 2048>
    None: typing.ClassVar[PieChartFlags]  # value = <PieChartFlags.None: 0>
    Normalize: typing.ClassVar[PieChartFlags]  # value = <PieChartFlags.Normalize: 1024>
    __members__: typing.ClassVar[dict[str, PieChartFlags]]  # value = {'None': <PieChartFlags.None: 0>, 'Normalize': <PieChartFlags.Normalize: 1024>, 'IgnoreHidden': <PieChartFlags.IgnoreHidden: 2048>, 'Exploding': <PieChartFlags.Exploding: 4096>}
    @typing.overload
    def __eq__(self, other: PieChartFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: PieChartFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Point:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _x: typing.SupportsFloat | typing.SupportsIndex, _y: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def x(self) -> float:
        ...
    @x.setter
    def x(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def y(self) -> float:
        ...
    @y.setter
    def y(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class Range:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _min: typing.SupportsFloat | typing.SupportsIndex, _max: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def max(self) -> float:
        ...
    @max.setter
    def max(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def min(self) -> float:
        ...
    @min.setter
    def min(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class Scale:
    """
    Members:
    
      ImPlotScale_Linear
    
      ImPlotScale_Time
    
      ImPlotScale_Log10
    
      ImPlotScale_SymLog
    """
    ImPlotScale_Linear: typing.ClassVar[Scale]  # value = <Scale.ImPlotScale_Linear: 0>
    ImPlotScale_Log10: typing.ClassVar[Scale]  # value = <Scale.ImPlotScale_Log10: 2>
    ImPlotScale_SymLog: typing.ClassVar[Scale]  # value = <Scale.ImPlotScale_SymLog: 3>
    ImPlotScale_Time: typing.ClassVar[Scale]  # value = <Scale.ImPlotScale_Time: 1>
    __members__: typing.ClassVar[dict[str, Scale]]  # value = {'ImPlotScale_Linear': <Scale.ImPlotScale_Linear: 0>, 'ImPlotScale_Time': <Scale.ImPlotScale_Time: 1>, 'ImPlotScale_Log10': <Scale.ImPlotScale_Log10: 2>, 'ImPlotScale_SymLog': <Scale.ImPlotScale_SymLog: 3>}
    @typing.overload
    def __eq__(self, other: Scale) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: Scale) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ScatterFlags:
    """
    Members:
    
      None
    
      NoClip
    """
    NoClip: typing.ClassVar[ScatterFlags]  # value = <ScatterFlags.NoClip: 1024>
    None: typing.ClassVar[ScatterFlags]  # value = <ScatterFlags.None: 0>
    __members__: typing.ClassVar[dict[str, ScatterFlags]]  # value = {'None': <ScatterFlags.None: 0>, 'NoClip': <ScatterFlags.NoClip: 1024>}
    @typing.overload
    def __eq__(self, other: ScatterFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: ScatterFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ShadedFlags:
    """
    Members:
    
      None
    """
    None: typing.ClassVar[ShadedFlags]  # value = <ShadedFlags.None: 0>
    __members__: typing.ClassVar[dict[str, ShadedFlags]]  # value = {'None': <ShadedFlags.None: 0>}
    @typing.overload
    def __eq__(self, other: ShadedFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: ShadedFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StairsFlags:
    """
    Members:
    
      None
    
      PreStep
    
      Shaded
    """
    None: typing.ClassVar[StairsFlags]  # value = <StairsFlags.None: 0>
    PreStep: typing.ClassVar[StairsFlags]  # value = <StairsFlags.PreStep: 1024>
    Shaded: typing.ClassVar[StairsFlags]  # value = <StairsFlags.Shaded: 2048>
    __members__: typing.ClassVar[dict[str, StairsFlags]]  # value = {'None': <StairsFlags.None: 0>, 'PreStep': <StairsFlags.PreStep: 1024>, 'Shaded': <StairsFlags.Shaded: 2048>}
    @typing.overload
    def __eq__(self, other: StairsFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: StairsFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StemsFlags:
    """
    Members:
    
      None
    
      Horizontal
    """
    Horizontal: typing.ClassVar[StemsFlags]  # value = <StemsFlags.Horizontal: 1024>
    None: typing.ClassVar[StemsFlags]  # value = <StemsFlags.None: 0>
    __members__: typing.ClassVar[dict[str, StemsFlags]]  # value = {'None': <StemsFlags.None: 0>, 'Horizontal': <StemsFlags.Horizontal: 1024>}
    @typing.overload
    def __eq__(self, other: StemsFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: StemsFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StyleVar:
    """
    Members:
    
      DigitalSpacing
    
      PlotBorderSize
    
      MinorAlpha
    
      MajorTickLen
    
      MinorTickLen
    
      MajorTickSize
    
      MinorTickSize
    
      MajorGridSize
    
      MinorGridSize
    
      PlotPadding
    
      LabelPadding
    
      LegendPadding
    
      LegendInnerPadding
    
      LegendSpacing
    
      MousePosPadding
    
      AnnotationPadding
    
      FitPadding
    
      PlotDefaultSize
    
      PlotMinSize
    
      DigitalPadding
    """
    AnnotationPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.AnnotationPadding: 16>
    DigitalPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.DigitalPadding: 18>
    DigitalSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.DigitalSpacing: 19>
    FitPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.FitPadding: 17>
    LabelPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.LabelPadding: 11>
    LegendInnerPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.LegendInnerPadding: 13>
    LegendPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.LegendPadding: 12>
    LegendSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.LegendSpacing: 14>
    MajorGridSize: typing.ClassVar[StyleVar]  # value = <StyleVar.MajorGridSize: 8>
    MajorTickLen: typing.ClassVar[StyleVar]  # value = <StyleVar.MajorTickLen: 4>
    MajorTickSize: typing.ClassVar[StyleVar]  # value = <StyleVar.MajorTickSize: 6>
    MinorAlpha: typing.ClassVar[StyleVar]  # value = <StyleVar.MinorAlpha: 3>
    MinorGridSize: typing.ClassVar[StyleVar]  # value = <StyleVar.MinorGridSize: 9>
    MinorTickLen: typing.ClassVar[StyleVar]  # value = <StyleVar.MinorTickLen: 5>
    MinorTickSize: typing.ClassVar[StyleVar]  # value = <StyleVar.MinorTickSize: 7>
    MousePosPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.MousePosPadding: 15>
    PlotBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.PlotBorderSize: 2>
    PlotDefaultSize: typing.ClassVar[StyleVar]  # value = <StyleVar.PlotDefaultSize: 0>
    PlotMinSize: typing.ClassVar[StyleVar]  # value = <StyleVar.PlotMinSize: 1>
    PlotPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.PlotPadding: 10>
    __members__: typing.ClassVar[dict[str, StyleVar]]  # value = {'DigitalSpacing': <StyleVar.DigitalSpacing: 19>, 'PlotBorderSize': <StyleVar.PlotBorderSize: 2>, 'MinorAlpha': <StyleVar.MinorAlpha: 3>, 'MajorTickLen': <StyleVar.MajorTickLen: 4>, 'MinorTickLen': <StyleVar.MinorTickLen: 5>, 'MajorTickSize': <StyleVar.MajorTickSize: 6>, 'MinorTickSize': <StyleVar.MinorTickSize: 7>, 'MajorGridSize': <StyleVar.MajorGridSize: 8>, 'MinorGridSize': <StyleVar.MinorGridSize: 9>, 'PlotPadding': <StyleVar.PlotPadding: 10>, 'LabelPadding': <StyleVar.LabelPadding: 11>, 'LegendPadding': <StyleVar.LegendPadding: 12>, 'LegendInnerPadding': <StyleVar.LegendInnerPadding: 13>, 'LegendSpacing': <StyleVar.LegendSpacing: 14>, 'MousePosPadding': <StyleVar.MousePosPadding: 15>, 'AnnotationPadding': <StyleVar.AnnotationPadding: 16>, 'FitPadding': <StyleVar.FitPadding: 17>, 'PlotDefaultSize': <StyleVar.PlotDefaultSize: 0>, 'PlotMinSize': <StyleVar.PlotMinSize: 1>, 'DigitalPadding': <StyleVar.DigitalPadding: 18>}
    @typing.overload
    def __eq__(self, other: StyleVar) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: StyleVar) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SubplotFlags:
    """
    Members:
    
      None
    
      NoTitle
    
      NoLegend
    
      NoMenus
    
      NoResize
    
      NoAlign
    
      ShareItems
    
      LinkRows
    
      LinkCols
    
      LinkAllX
    
      LinkAllY
    
      ColMajor
    """
    ColMajor: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.ColMajor: 1024>
    LinkAllX: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.LinkAllX: 256>
    LinkAllY: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.LinkAllY: 512>
    LinkCols: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.LinkCols: 128>
    LinkRows: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.LinkRows: 64>
    NoAlign: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.NoAlign: 16>
    NoLegend: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.NoLegend: 2>
    NoMenus: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.NoMenus: 4>
    NoResize: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.NoResize: 8>
    NoTitle: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.NoTitle: 1>
    None: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.None: 0>
    ShareItems: typing.ClassVar[SubplotFlags]  # value = <SubplotFlags.ShareItems: 32>
    __members__: typing.ClassVar[dict[str, SubplotFlags]]  # value = {'None': <SubplotFlags.None: 0>, 'NoTitle': <SubplotFlags.NoTitle: 1>, 'NoLegend': <SubplotFlags.NoLegend: 2>, 'NoMenus': <SubplotFlags.NoMenus: 4>, 'NoResize': <SubplotFlags.NoResize: 8>, 'NoAlign': <SubplotFlags.NoAlign: 16>, 'ShareItems': <SubplotFlags.ShareItems: 32>, 'LinkRows': <SubplotFlags.LinkRows: 64>, 'LinkCols': <SubplotFlags.LinkCols: 128>, 'LinkAllX': <SubplotFlags.LinkAllX: 256>, 'LinkAllY': <SubplotFlags.LinkAllY: 512>, 'ColMajor': <SubplotFlags.ColMajor: 1024>}
    @typing.overload
    def __eq__(self, other: SubplotFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: SubplotFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TextFlags:
    """
    Members:
    
      None
    
      Vertical
    """
    None: typing.ClassVar[TextFlags]  # value = <TextFlags.None: 0>
    Vertical: typing.ClassVar[TextFlags]  # value = <TextFlags.Vertical: 1024>
    __members__: typing.ClassVar[dict[str, TextFlags]]  # value = {'None': <TextFlags.None: 0>, 'Vertical': <TextFlags.Vertical: 1024>}
    @typing.overload
    def __eq__(self, other: TextFlags) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    @typing.overload
    def __ne__(self, other: TextFlags) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @typing.overload
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
@typing.overload
def Annotation(x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, pix_offset: mujoco.studio.dear_imgui.dear_imgui.Vec2, clamp: bool, round: bool = False) -> None:
    ...
@typing.overload
def Annotation(x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, pix_offset: mujoco.studio.dear_imgui.dear_imgui.Vec2, clamp: bool, txt: str) -> None:
    ...
def BeginAlignedPlots(group_id: str, vertical: bool = True) -> bool:
    ...
def BeginDragDropSourceAxis(axis: typing.SupportsInt | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginDragDropSourceItem(label_id: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginDragDropSourcePlot(flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginDragDropTargetAxis(axis: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def BeginDragDropTargetLegend() -> bool:
    ...
def BeginDragDropTargetPlot() -> bool:
    ...
def BeginLegendPopup(label_id: str, mouse_button: typing.SupportsInt | typing.SupportsIndex = 1) -> bool:
    ...
def BeginPlot(title_id: str, size: mujoco.studio.dear_imgui.dear_imgui.Vec2 = ..., flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginSubplots(title_id: str, rows: typing.SupportsInt | typing.SupportsIndex, cols: typing.SupportsInt | typing.SupportsIndex, size: mujoco.studio.dear_imgui.dear_imgui.Vec2, flags: typing.SupportsInt | typing.SupportsIndex = 0, row_ratios: typing.SupportsFloat | typing.SupportsIndex = None, col_ratios: typing.SupportsFloat | typing.SupportsIndex = None) -> bool:
    ...
def CancelPlotSelection() -> None:
    ...
def CreateContext() -> int:
    """
    Creates a context and makes it current; returns its handle.
    """
def DestroyContext(ptr: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    """
    Destroys the given context (0: the current one).
    """
def DragLineX(id: typing.SupportsInt | typing.SupportsIndex, x: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, thickness: typing.SupportsFloat | typing.SupportsIndex = 1, flags: typing.SupportsInt | typing.SupportsIndex = 0, out_clicked: bool = None, out_hovered: bool = None, out_held: bool = None) -> bool:
    ...
def DragLineY(id: typing.SupportsInt | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, thickness: typing.SupportsFloat | typing.SupportsIndex = 1, flags: typing.SupportsInt | typing.SupportsIndex = 0, out_clicked: bool = None, out_hovered: bool = None, out_held: bool = None) -> bool:
    ...
def DragPoint(id: typing.SupportsInt | typing.SupportsIndex, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, size: typing.SupportsFloat | typing.SupportsIndex = 4, flags: typing.SupportsInt | typing.SupportsIndex = 0, out_clicked: bool = None, out_hovered: bool = None, out_held: bool = None) -> bool:
    ...
def DragRect(id: typing.SupportsInt | typing.SupportsIndex, x1: typing.SupportsFloat | typing.SupportsIndex, y1: typing.SupportsFloat | typing.SupportsIndex, x2: typing.SupportsFloat | typing.SupportsIndex, y2: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, flags: typing.SupportsInt | typing.SupportsIndex = 0, out_clicked: bool = None, out_hovered: bool = None, out_held: bool = None) -> bool:
    ...
def EndAlignedPlots() -> None:
    ...
def EndDragDropSource() -> None:
    ...
def EndDragDropTarget() -> None:
    ...
def EndLegendPopup() -> None:
    ...
def EndPlot() -> None:
    ...
def EndSubplots() -> None:
    ...
def GetPlotLimits(x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> ImPlotRect:
    ...
def GetPlotMousePos(x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> Point:
    ...
def GetPlotPos() -> mujoco.studio.dear_imgui.dear_imgui.Vec2:
    ...
def GetPlotSelection(x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> ImPlotRect:
    ...
def GetPlotSize() -> mujoco.studio.dear_imgui.dear_imgui.Vec2:
    ...
def HideNextItem(hidden: bool = True, cond: typing.SupportsInt | typing.SupportsIndex = ...) -> None:
    ...
def IsAxisHovered(axis: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def IsLegendEntryHovered(label_id: str) -> bool:
    ...
def IsPlotHovered() -> bool:
    ...
def IsPlotSelected() -> bool:
    ...
def IsSubplotsHovered() -> bool:
    ...
@typing.overload
def PixelsToPlot(pix: mujoco.studio.dear_imgui.dear_imgui.Vec2, x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> Point:
    ...
@typing.overload
def PixelsToPlot(x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> Point:
    ...
def PlotBars(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], bar_size: typing.SupportsFloat | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotDigital(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotDummy(label_id: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def PlotErrorBars(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], err: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
@typing.overload
def PlotErrorBars(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], neg: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], pos: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotImage(label_id: str, tex_ref: ImTextureRef, bounds_min: Point, bounds_max: Point, uv0: mujoco.studio.dear_imgui.dear_imgui.Vec2 = ..., uv1: mujoco.studio.dear_imgui.dear_imgui.Vec2 = ..., tint_col: mujoco.studio.dear_imgui.dear_imgui.Vec4 = ..., flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def PlotLine(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotScatter(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
@typing.overload
def PlotShaded(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], yref: typing.SupportsFloat | typing.SupportsIndex = 0, flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
@typing.overload
def PlotShaded(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys1: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys2: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotStairs(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotStems(label_id: str, xs: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ys: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ref: typing.SupportsFloat | typing.SupportsIndex = 0, flags: typing.SupportsInt | typing.SupportsIndex = 0, offset: typing.SupportsInt | typing.SupportsIndex = 0, stride: typing.SupportsInt | typing.SupportsIndex = 8) -> None:
    ...
def PlotText(text: str, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, pix_offset: mujoco.studio.dear_imgui.dear_imgui.Vec2 = ..., flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def PlotToPixels(plt: Point, x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> mujoco.studio.dear_imgui.dear_imgui.Vec2:
    ...
@typing.overload
def PlotToPixels(x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, x_axis: typing.SupportsInt | typing.SupportsIndex = -1, y_axis: typing.SupportsInt | typing.SupportsIndex = -1) -> mujoco.studio.dear_imgui.dear_imgui.Vec2:
    ...
def PopPlotClipRect() -> None:
    ...
def PopStyleColor(count: typing.SupportsInt | typing.SupportsIndex = 1) -> None:
    ...
def PopStyleVar(count: typing.SupportsInt | typing.SupportsIndex = 1) -> None:
    ...
def PushPlotClipRect(expand: typing.SupportsFloat | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def PushStyleColor(idx: typing.SupportsInt | typing.SupportsIndex, col: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
@typing.overload
def PushStyleColor(idx: typing.SupportsInt | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4) -> None:
    ...
@typing.overload
def PushStyleVar(idx: typing.SupportsInt | typing.SupportsIndex, val: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
@typing.overload
def PushStyleVar(idx: typing.SupportsInt | typing.SupportsIndex, val: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
@typing.overload
def PushStyleVar(idx: typing.SupportsInt | typing.SupportsIndex, val: mujoco.studio.dear_imgui.dear_imgui.Vec2) -> None:
    ...
def SetAxes(x_axis: typing.SupportsInt | typing.SupportsIndex, y_axis: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetAxis(axis: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetNextAxesLimits(x_min: typing.SupportsFloat | typing.SupportsIndex, x_max: typing.SupportsFloat | typing.SupportsIndex, y_min: typing.SupportsFloat | typing.SupportsIndex, y_max: typing.SupportsFloat | typing.SupportsIndex, cond: typing.SupportsInt | typing.SupportsIndex = ...) -> None:
    ...
def SetNextAxesToFit() -> None:
    ...
def SetNextAxisLimits(axis: typing.SupportsInt | typing.SupportsIndex, v_min: typing.SupportsFloat | typing.SupportsIndex, v_max: typing.SupportsFloat | typing.SupportsIndex, cond: typing.SupportsInt | typing.SupportsIndex = ...) -> None:
    ...
def SetNextAxisLinks(axis: typing.SupportsInt | typing.SupportsIndex, link_min: typing.SupportsFloat | typing.SupportsIndex, link_max: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetNextAxisToFit(axis: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetupAxes(x_label: str, y_label: str, x_flags: typing.SupportsInt | typing.SupportsIndex = 0, y_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetupAxesLimits(x_min: typing.SupportsFloat | typing.SupportsIndex, x_max: typing.SupportsFloat | typing.SupportsIndex, y_min: typing.SupportsFloat | typing.SupportsIndex, y_max: typing.SupportsFloat | typing.SupportsIndex, cond: typing.SupportsInt | typing.SupportsIndex = ...) -> None:
    ...
def SetupAxis(axis: typing.SupportsInt | typing.SupportsIndex, label: str = None, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetupAxisFormat(axis: typing.SupportsInt | typing.SupportsIndex, fmt: str) -> None:
    ...
def SetupAxisLimits(axis: typing.SupportsInt | typing.SupportsIndex, v_min: typing.SupportsFloat | typing.SupportsIndex, v_max: typing.SupportsFloat | typing.SupportsIndex, cond: typing.SupportsInt | typing.SupportsIndex = ...) -> None:
    ...
def SetupAxisLimitsConstraints(axis: typing.SupportsInt | typing.SupportsIndex, v_min: typing.SupportsFloat | typing.SupportsIndex, v_max: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetupAxisLinks(axis: typing.SupportsInt | typing.SupportsIndex, link_min: typing.SupportsFloat | typing.SupportsIndex, link_max: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetupAxisScale(axis: typing.SupportsInt | typing.SupportsIndex, scale: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetupAxisTicks(axis: typing.SupportsInt | typing.SupportsIndex, values: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], labels: collections.abc.Sequence[str], keep_default: bool = False) -> None:
    ...
def SetupAxisZoomConstraints(axis: typing.SupportsInt | typing.SupportsIndex, z_min: typing.SupportsFloat | typing.SupportsIndex, z_max: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetupFinish() -> None:
    ...
def SetupLegend(location: typing.SupportsInt | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetupMouseText(location: typing.SupportsInt | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def TagX(x: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, round: bool = False) -> None:
    ...
@typing.overload
def TagX(x: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, txt: str) -> None:
    ...
@typing.overload
def TagY(y: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, round: bool = False) -> None:
    ...
@typing.overload
def TagY(y: typing.SupportsFloat | typing.SupportsIndex, col: mujoco.studio.dear_imgui.dear_imgui.Vec4, txt: str) -> None:
    ...
def set_imgui_context(ptr: typing.SupportsInt | typing.SupportsIndex) -> None:
    """
    Set ImGui context pointer.
    """
def set_implot_context(ptr: typing.SupportsInt | typing.SupportsIndex) -> None:
    """
    Set ImPlot context pointer.
    """
