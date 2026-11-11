from __future__ import annotations
import collections.abc
import typing
__all__: list[str] = ['AlignTextToFramePadding', 'ArrowButton', 'BackendFlags', 'Begin', 'BeginChild', 'BeginChildId', 'BeginCombo', 'BeginDisabled', 'BeginGroup', 'BeginItemTooltip', 'BeginListBox', 'BeginMainMenuBar', 'BeginMenu', 'BeginMenuBar', 'BeginPopup', 'BeginPopupContextItem', 'BeginPopupContextVoid', 'BeginPopupContextWindow', 'BeginPopupModal', 'BeginTabBar', 'BeginTabItem', 'BeginTable', 'BeginTooltip', 'Bullet', 'BulletText', 'Button', 'ButtonFlags', 'CalcItemWidth', 'CalcTextSize', 'Checkbox', 'ChildFlags', 'CloseCurrentPopup', 'Col', 'CollapsingHeader', 'CollapsingHeader2', 'ColorButton', 'ColorConvertFloat4ToU32', 'ColorConvertHSVtoRGB', 'ColorConvertRGBtoHSV', 'ColorConvertU32ToFloat4', 'ColorEdit3', 'ColorEdit4', 'ColorEditFlags', 'ColorPicker3', 'ColorPicker4', 'Columns', 'Combo', 'ComboFlags', 'ComboStr', 'Cond', 'ConfigFlags', 'CreateContext', 'DataType', 'DestroyContext', 'Dir', 'DockBuilderAddNode', 'DockBuilderDockWindow', 'DockBuilderFinish', 'DockBuilderGetNode', 'DockBuilderRemoveNode', 'DockBuilderSetNodeSize', 'DockBuilderSplitNode', 'DockNodeFlags', 'DockSpace', 'DockSpaceOverMainViewport', 'DragDropFlags', 'DragFloat', 'DragFloatN', 'DragInt', 'DragIntN', 'DrawFlags', 'DrawList', 'Dummy', 'End', 'EndChild', 'EndCombo', 'EndDisabled', 'EndFrame', 'EndGroup', 'EndListBox', 'EndMainMenuBar', 'EndMenu', 'EndMenuBar', 'EndPopup', 'EndTabBar', 'EndTabItem', 'EndTable', 'EndTooltip', 'FocusedFlags', 'Font', 'FontAtlas', 'GetBackgroundDrawList', 'GetClipboardText', 'GetColorU32', 'GetColumnIndex', 'GetColumnOffset', 'GetColumnWidth', 'GetColumnsCount', 'GetContentRegionAvail', 'GetContentRegionMax', 'GetCurrentContext', 'GetCursorPos', 'GetCursorPosX', 'GetCursorPosY', 'GetCursorScreenPos', 'GetCursorStartPos', 'GetFontSize', 'GetFontTexUvWhitePixel', 'GetForegroundDrawList', 'GetFrameCount', 'GetFrameHeight', 'GetFrameHeightWithSpacing', 'GetID', 'GetIO', 'GetItemID', 'GetItemRectMax', 'GetItemRectMin', 'GetItemRectSize', 'GetKeyName', 'GetKeyPressedAmount', 'GetMouseClickedCount', 'GetMouseCursor', 'GetMouseDragDelta', 'GetMousePos', 'GetMousePosOnOpeningCurrentPopup', 'GetScrollMaxX', 'GetScrollMaxY', 'GetScrollX', 'GetScrollY', 'GetStyle', 'GetStyleColorVec4', 'GetTextLineHeight', 'GetTextLineHeightWithSpacing', 'GetTime', 'GetTreeNodeToLabelSpacing', 'GetWindowContentRegionMax', 'GetWindowContentRegionMin', 'GetWindowDockID', 'GetWindowDpiScale', 'GetWindowDrawList', 'GetWindowHeight', 'GetWindowPos', 'GetWindowSize', 'GetWindowWidth', 'HoveredFlags', 'IO', 'Image', 'ImageButton', 'Indent', 'InputDouble', 'InputFlags', 'InputFloat', 'InputFloatN', 'InputInt', 'InputIntN', 'InputText', 'InputTextFlags', 'InputTextMultiline', 'InputTextWithHint', 'InvisibleButton', 'IsAnyItemActive', 'IsAnyItemFocused', 'IsAnyItemHovered', 'IsAnyMouseDown', 'IsItemActivated', 'IsItemActive', 'IsItemClicked', 'IsItemDeactivated', 'IsItemDeactivatedAfterEdit', 'IsItemEdited', 'IsItemFocused', 'IsItemHovered', 'IsItemToggledOpen', 'IsItemVisible', 'IsKeyChordPressed', 'IsKeyDown', 'IsKeyPressed', 'IsKeyReleased', 'IsMouseClicked', 'IsMouseDoubleClicked', 'IsMouseDown', 'IsMouseDragging', 'IsMouseHoveringRect', 'IsMousePosValid', 'IsMouseReleased', 'IsPopupOpen', 'IsRectVisible', 'IsWindowAppearing', 'IsWindowCollapsed', 'IsWindowDocked', 'IsWindowFocused', 'IsWindowHovered', 'Key', 'LabelText', 'ListClipper', 'MenuItem', 'MouseButton', 'MouseCursor', 'MouseSource', 'NewFrame', 'NewLine', 'NextColumn', 'OpenPopup', 'OpenPopupOnItemClick', 'PopButtonRepeat', 'PopClipRect', 'PopFont', 'PopID', 'PopItemWidth', 'PopStyleColor', 'PopStyleVar', 'PopTabStop', 'PopTextWrapPos', 'PopupFlags', 'ProgressBar', 'PushButtonRepeat', 'PushClipRect', 'PushFont', 'PushID', 'PushItemWidth', 'PushStyleColor', 'PushStyleVar', 'PushTabStop', 'PushTextWrapPos', 'RadioButton', 'Render', 'ResetMouseDragDelta', 'SameLine', 'Selectable', 'Selectable2', 'SelectableFlags', 'Separator', 'SeparatorText', 'SetClipboardText', 'SetColorEditOptions', 'SetColumnOffset', 'SetColumnWidth', 'SetCurrentContext', 'SetCursorPos', 'SetCursorPosX', 'SetCursorPosY', 'SetCursorScreenPos', 'SetItemDefaultFocus', 'SetItemTooltip', 'SetKeyboardFocusHere', 'SetMouseCursor', 'SetNextFrameWantCaptureKeyboard', 'SetNextFrameWantCaptureMouse', 'SetNextItemAllowOverlap', 'SetNextItemOpen', 'SetNextItemShortcut', 'SetNextItemWidth', 'SetNextWindowBgAlpha', 'SetNextWindowCollapsed', 'SetNextWindowContentSize', 'SetNextWindowDockID', 'SetNextWindowFocus', 'SetNextWindowPos', 'SetNextWindowScroll', 'SetNextWindowSize', 'SetNextWindowSizeConstraints', 'SetNextWindowViewport', 'SetScrollFromPosX', 'SetScrollFromPosY', 'SetScrollHereX', 'SetScrollHereY', 'SetScrollX', 'SetScrollY', 'SetTabItemClosed', 'SetTooltip', 'SetWindowCollapsed', 'SetWindowFocus', 'SetWindowFontScale', 'SetWindowPos', 'SetWindowSize', 'Shortcut', 'ShowDemoWindow', 'SliderAngle', 'SliderFlags', 'SliderFloat', 'SliderFloatN', 'SliderInt', 'SliderIntN', 'SmallButton', 'SortDirection', 'Spacing', 'Style', 'StyleColorsClassic', 'StyleColorsDark', 'StyleColorsLight', 'StyleVar', 'TabBarFlags', 'TabItemButton', 'TabItemFlags', 'TableAngledHeadersRow', 'TableBgTarget', 'TableColumnFlags', 'TableFlags', 'TableGetColumnCount', 'TableGetColumnFlags', 'TableGetColumnIndex', 'TableGetColumnName', 'TableGetHoveredColumn', 'TableGetRowIndex', 'TableHeader', 'TableHeadersRow', 'TableNextColumn', 'TableNextRow', 'TableRowFlags', 'TableSetBgColor', 'TableSetColumnEnabled', 'TableSetColumnIndex', 'TableSetupColumn', 'TableSetupScrollFreeze', 'Text', 'TextColored', 'TextDisabled', 'TextLink', 'TextLinkOpenURL', 'TextUnformatted', 'TextWrapped', 'TreeNode', 'TreeNodeEx', 'TreeNodeFlags', 'TreePop', 'TreePush', 'Unindent', 'Value', 'Vec2', 'Vec4', 'WindowFlags']
class BackendFlags:
    """
    Members:
    
      None
    
      HasGamepad
    
      HasMouseCursors
    
      HasSetMousePos
    
      RendererHasVtxOffset
    
      RendererHasTextures
    
      PlatformHasViewports
    
      HasMouseHoveredViewport
    
      RendererHasViewports
    """
    HasGamepad: typing.ClassVar[BackendFlags]  # value = <BackendFlags.HasGamepad: 1>
    HasMouseCursors: typing.ClassVar[BackendFlags]  # value = <BackendFlags.HasMouseCursors: 2>
    HasMouseHoveredViewport: typing.ClassVar[BackendFlags]  # value = <BackendFlags.HasMouseHoveredViewport: 4096>
    HasSetMousePos: typing.ClassVar[BackendFlags]  # value = <BackendFlags.HasSetMousePos: 4>
    None: typing.ClassVar[BackendFlags]  # value = <BackendFlags.None: 0>
    PlatformHasViewports: typing.ClassVar[BackendFlags]  # value = <BackendFlags.PlatformHasViewports: 2048>
    RendererHasTextures: typing.ClassVar[BackendFlags]  # value = <BackendFlags.RendererHasTextures: 16>
    RendererHasViewports: typing.ClassVar[BackendFlags]  # value = <BackendFlags.RendererHasViewports: 1024>
    RendererHasVtxOffset: typing.ClassVar[BackendFlags]  # value = <BackendFlags.RendererHasVtxOffset: 8>
    __members__: typing.ClassVar[dict[str, BackendFlags]]  # value = {'None': <BackendFlags.None: 0>, 'HasGamepad': <BackendFlags.HasGamepad: 1>, 'HasMouseCursors': <BackendFlags.HasMouseCursors: 2>, 'HasSetMousePos': <BackendFlags.HasSetMousePos: 4>, 'RendererHasVtxOffset': <BackendFlags.RendererHasVtxOffset: 8>, 'RendererHasTextures': <BackendFlags.RendererHasTextures: 16>, 'PlatformHasViewports': <BackendFlags.PlatformHasViewports: 2048>, 'HasMouseHoveredViewport': <BackendFlags.HasMouseHoveredViewport: 4096>, 'RendererHasViewports': <BackendFlags.RendererHasViewports: 1024>}
    @typing.overload
    def __eq__(self, other: BackendFlags) -> bool:
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
    def __ne__(self, other: BackendFlags) -> bool:
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
class ButtonFlags:
    """
    Members:
    
      None
    
      MouseButtonLeft
    
      MouseButtonRight
    
      MouseButtonMiddle
    
      MouseButtonMask
    """
    MouseButtonLeft: typing.ClassVar[ButtonFlags]  # value = <ButtonFlags.MouseButtonLeft: 1>
    MouseButtonMask: typing.ClassVar[ButtonFlags]  # value = <ButtonFlags.MouseButtonMask: 7>
    MouseButtonMiddle: typing.ClassVar[ButtonFlags]  # value = <ButtonFlags.MouseButtonMiddle: 4>
    MouseButtonRight: typing.ClassVar[ButtonFlags]  # value = <ButtonFlags.MouseButtonRight: 2>
    None: typing.ClassVar[ButtonFlags]  # value = <ButtonFlags.None: 0>
    __members__: typing.ClassVar[dict[str, ButtonFlags]]  # value = {'None': <ButtonFlags.None: 0>, 'MouseButtonLeft': <ButtonFlags.MouseButtonLeft: 1>, 'MouseButtonRight': <ButtonFlags.MouseButtonRight: 2>, 'MouseButtonMiddle': <ButtonFlags.MouseButtonMiddle: 4>, 'MouseButtonMask': <ButtonFlags.MouseButtonMask: 7>}
    @typing.overload
    def __eq__(self, other: ButtonFlags) -> bool:
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
    def __ne__(self, other: ButtonFlags) -> bool:
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
class ChildFlags:
    """
    Members:
    
      None
    
      Borders
    
      AlwaysUseWindowPadding
    
      ResizeX
    
      ResizeY
    
      AutoResizeX
    
      AutoResizeY
    
      AlwaysAutoResize
    
      FrameStyle
    
      NavFlattened
    """
    AlwaysAutoResize: typing.ClassVar[ChildFlags]  # value = <ChildFlags.AlwaysAutoResize: 64>
    AlwaysUseWindowPadding: typing.ClassVar[ChildFlags]  # value = <ChildFlags.AlwaysUseWindowPadding: 2>
    AutoResizeX: typing.ClassVar[ChildFlags]  # value = <ChildFlags.AutoResizeX: 16>
    AutoResizeY: typing.ClassVar[ChildFlags]  # value = <ChildFlags.AutoResizeY: 32>
    Borders: typing.ClassVar[ChildFlags]  # value = <ChildFlags.Borders: 1>
    FrameStyle: typing.ClassVar[ChildFlags]  # value = <ChildFlags.FrameStyle: 128>
    NavFlattened: typing.ClassVar[ChildFlags]  # value = <ChildFlags.NavFlattened: 256>
    None: typing.ClassVar[ChildFlags]  # value = <ChildFlags.None: 0>
    ResizeX: typing.ClassVar[ChildFlags]  # value = <ChildFlags.ResizeX: 4>
    ResizeY: typing.ClassVar[ChildFlags]  # value = <ChildFlags.ResizeY: 8>
    __members__: typing.ClassVar[dict[str, ChildFlags]]  # value = {'None': <ChildFlags.None: 0>, 'Borders': <ChildFlags.Borders: 1>, 'AlwaysUseWindowPadding': <ChildFlags.AlwaysUseWindowPadding: 2>, 'ResizeX': <ChildFlags.ResizeX: 4>, 'ResizeY': <ChildFlags.ResizeY: 8>, 'AutoResizeX': <ChildFlags.AutoResizeX: 16>, 'AutoResizeY': <ChildFlags.AutoResizeY: 32>, 'AlwaysAutoResize': <ChildFlags.AlwaysAutoResize: 64>, 'FrameStyle': <ChildFlags.FrameStyle: 128>, 'NavFlattened': <ChildFlags.NavFlattened: 256>}
    @typing.overload
    def __eq__(self, other: ChildFlags) -> bool:
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
    def __ne__(self, other: ChildFlags) -> bool:
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
    
      Text
    
      TextDisabled
    
      WindowBg
    
      ChildBg
    
      PopupBg
    
      Border
    
      BorderShadow
    
      FrameBg
    
      FrameBgHovered
    
      FrameBgActive
    
      TitleBg
    
      TitleBgActive
    
      TitleBgCollapsed
    
      MenuBarBg
    
      ScrollbarBg
    
      ScrollbarGrab
    
      ScrollbarGrabHovered
    
      ScrollbarGrabActive
    
      CheckMark
    
      SliderGrab
    
      SliderGrabActive
    
      Button
    
      ButtonHovered
    
      ButtonActive
    
      Header
    
      HeaderHovered
    
      HeaderActive
    
      Separator
    
      SeparatorHovered
    
      SeparatorActive
    
      ResizeGrip
    
      ResizeGripHovered
    
      ResizeGripActive
    
      TabHovered
    
      Tab
    
      TabSelected
    
      TabSelectedOverline
    
      TabDimmed
    
      TabDimmedSelected
    
      TabDimmedSelectedOverline
    
      DockingPreview
    
      DockingEmptyBg
    
      PlotLines
    
      PlotLinesHovered
    
      PlotHistogram
    
      PlotHistogramHovered
    
      TableHeaderBg
    
      TableBorderStrong
    
      TableBorderLight
    
      TableRowBg
    
      TableRowBgAlt
    
      TextLink
    
      TextSelectedBg
    
      DragDropTarget
    
      NavHighlight
    
      NavWindowingHighlight
    
      NavWindowingDimBg
    
      ModalWindowDimBg
    """
    Border: typing.ClassVar[Col]  # value = <Col.Border: 5>
    BorderShadow: typing.ClassVar[Col]  # value = <Col.BorderShadow: 6>
    Button: typing.ClassVar[Col]  # value = <Col.Button: 22>
    ButtonActive: typing.ClassVar[Col]  # value = <Col.ButtonActive: 24>
    ButtonHovered: typing.ClassVar[Col]  # value = <Col.ButtonHovered: 23>
    CheckMark: typing.ClassVar[Col]  # value = <Col.CheckMark: 18>
    ChildBg: typing.ClassVar[Col]  # value = <Col.ChildBg: 3>
    DockingEmptyBg: typing.ClassVar[Col]  # value = <Col.DockingEmptyBg: 43>
    DockingPreview: typing.ClassVar[Col]  # value = <Col.DockingPreview: 42>
    DragDropTarget: typing.ClassVar[Col]  # value = <Col.DragDropTarget: 56>
    FrameBg: typing.ClassVar[Col]  # value = <Col.FrameBg: 7>
    FrameBgActive: typing.ClassVar[Col]  # value = <Col.FrameBgActive: 9>
    FrameBgHovered: typing.ClassVar[Col]  # value = <Col.FrameBgHovered: 8>
    Header: typing.ClassVar[Col]  # value = <Col.Header: 25>
    HeaderActive: typing.ClassVar[Col]  # value = <Col.HeaderActive: 27>
    HeaderHovered: typing.ClassVar[Col]  # value = <Col.HeaderHovered: 26>
    MenuBarBg: typing.ClassVar[Col]  # value = <Col.MenuBarBg: 13>
    ModalWindowDimBg: typing.ClassVar[Col]  # value = <Col.ModalWindowDimBg: 62>
    NavHighlight: typing.ClassVar[Col]  # value = <Col.NavHighlight: 59>
    NavWindowingDimBg: typing.ClassVar[Col]  # value = <Col.NavWindowingDimBg: 61>
    NavWindowingHighlight: typing.ClassVar[Col]  # value = <Col.NavWindowingHighlight: 60>
    PlotHistogram: typing.ClassVar[Col]  # value = <Col.PlotHistogram: 46>
    PlotHistogramHovered: typing.ClassVar[Col]  # value = <Col.PlotHistogramHovered: 47>
    PlotLines: typing.ClassVar[Col]  # value = <Col.PlotLines: 44>
    PlotLinesHovered: typing.ClassVar[Col]  # value = <Col.PlotLinesHovered: 45>
    PopupBg: typing.ClassVar[Col]  # value = <Col.PopupBg: 4>
    ResizeGrip: typing.ClassVar[Col]  # value = <Col.ResizeGrip: 31>
    ResizeGripActive: typing.ClassVar[Col]  # value = <Col.ResizeGripActive: 33>
    ResizeGripHovered: typing.ClassVar[Col]  # value = <Col.ResizeGripHovered: 32>
    ScrollbarBg: typing.ClassVar[Col]  # value = <Col.ScrollbarBg: 14>
    ScrollbarGrab: typing.ClassVar[Col]  # value = <Col.ScrollbarGrab: 15>
    ScrollbarGrabActive: typing.ClassVar[Col]  # value = <Col.ScrollbarGrabActive: 17>
    ScrollbarGrabHovered: typing.ClassVar[Col]  # value = <Col.ScrollbarGrabHovered: 16>
    Separator: typing.ClassVar[Col]  # value = <Col.Separator: 28>
    SeparatorActive: typing.ClassVar[Col]  # value = <Col.SeparatorActive: 30>
    SeparatorHovered: typing.ClassVar[Col]  # value = <Col.SeparatorHovered: 29>
    SliderGrab: typing.ClassVar[Col]  # value = <Col.SliderGrab: 20>
    SliderGrabActive: typing.ClassVar[Col]  # value = <Col.SliderGrabActive: 21>
    Tab: typing.ClassVar[Col]  # value = <Col.Tab: 36>
    TabDimmed: typing.ClassVar[Col]  # value = <Col.TabDimmed: 39>
    TabDimmedSelected: typing.ClassVar[Col]  # value = <Col.TabDimmedSelected: 40>
    TabDimmedSelectedOverline: typing.ClassVar[Col]  # value = <Col.TabDimmedSelectedOverline: 41>
    TabHovered: typing.ClassVar[Col]  # value = <Col.TabHovered: 35>
    TabSelected: typing.ClassVar[Col]  # value = <Col.TabSelected: 37>
    TabSelectedOverline: typing.ClassVar[Col]  # value = <Col.TabSelectedOverline: 38>
    TableBorderLight: typing.ClassVar[Col]  # value = <Col.TableBorderLight: 50>
    TableBorderStrong: typing.ClassVar[Col]  # value = <Col.TableBorderStrong: 49>
    TableHeaderBg: typing.ClassVar[Col]  # value = <Col.TableHeaderBg: 48>
    TableRowBg: typing.ClassVar[Col]  # value = <Col.TableRowBg: 51>
    TableRowBgAlt: typing.ClassVar[Col]  # value = <Col.TableRowBgAlt: 52>
    Text: typing.ClassVar[Col]  # value = <Col.Text: 0>
    TextDisabled: typing.ClassVar[Col]  # value = <Col.TextDisabled: 1>
    TextLink: typing.ClassVar[Col]  # value = <Col.TextLink: 53>
    TextSelectedBg: typing.ClassVar[Col]  # value = <Col.TextSelectedBg: 54>
    TitleBg: typing.ClassVar[Col]  # value = <Col.TitleBg: 10>
    TitleBgActive: typing.ClassVar[Col]  # value = <Col.TitleBgActive: 11>
    TitleBgCollapsed: typing.ClassVar[Col]  # value = <Col.TitleBgCollapsed: 12>
    WindowBg: typing.ClassVar[Col]  # value = <Col.WindowBg: 2>
    __members__: typing.ClassVar[dict[str, Col]]  # value = {'Text': <Col.Text: 0>, 'TextDisabled': <Col.TextDisabled: 1>, 'WindowBg': <Col.WindowBg: 2>, 'ChildBg': <Col.ChildBg: 3>, 'PopupBg': <Col.PopupBg: 4>, 'Border': <Col.Border: 5>, 'BorderShadow': <Col.BorderShadow: 6>, 'FrameBg': <Col.FrameBg: 7>, 'FrameBgHovered': <Col.FrameBgHovered: 8>, 'FrameBgActive': <Col.FrameBgActive: 9>, 'TitleBg': <Col.TitleBg: 10>, 'TitleBgActive': <Col.TitleBgActive: 11>, 'TitleBgCollapsed': <Col.TitleBgCollapsed: 12>, 'MenuBarBg': <Col.MenuBarBg: 13>, 'ScrollbarBg': <Col.ScrollbarBg: 14>, 'ScrollbarGrab': <Col.ScrollbarGrab: 15>, 'ScrollbarGrabHovered': <Col.ScrollbarGrabHovered: 16>, 'ScrollbarGrabActive': <Col.ScrollbarGrabActive: 17>, 'CheckMark': <Col.CheckMark: 18>, 'SliderGrab': <Col.SliderGrab: 20>, 'SliderGrabActive': <Col.SliderGrabActive: 21>, 'Button': <Col.Button: 22>, 'ButtonHovered': <Col.ButtonHovered: 23>, 'ButtonActive': <Col.ButtonActive: 24>, 'Header': <Col.Header: 25>, 'HeaderHovered': <Col.HeaderHovered: 26>, 'HeaderActive': <Col.HeaderActive: 27>, 'Separator': <Col.Separator: 28>, 'SeparatorHovered': <Col.SeparatorHovered: 29>, 'SeparatorActive': <Col.SeparatorActive: 30>, 'ResizeGrip': <Col.ResizeGrip: 31>, 'ResizeGripHovered': <Col.ResizeGripHovered: 32>, 'ResizeGripActive': <Col.ResizeGripActive: 33>, 'TabHovered': <Col.TabHovered: 35>, 'Tab': <Col.Tab: 36>, 'TabSelected': <Col.TabSelected: 37>, 'TabSelectedOverline': <Col.TabSelectedOverline: 38>, 'TabDimmed': <Col.TabDimmed: 39>, 'TabDimmedSelected': <Col.TabDimmedSelected: 40>, 'TabDimmedSelectedOverline': <Col.TabDimmedSelectedOverline: 41>, 'DockingPreview': <Col.DockingPreview: 42>, 'DockingEmptyBg': <Col.DockingEmptyBg: 43>, 'PlotLines': <Col.PlotLines: 44>, 'PlotLinesHovered': <Col.PlotLinesHovered: 45>, 'PlotHistogram': <Col.PlotHistogram: 46>, 'PlotHistogramHovered': <Col.PlotHistogramHovered: 47>, 'TableHeaderBg': <Col.TableHeaderBg: 48>, 'TableBorderStrong': <Col.TableBorderStrong: 49>, 'TableBorderLight': <Col.TableBorderLight: 50>, 'TableRowBg': <Col.TableRowBg: 51>, 'TableRowBgAlt': <Col.TableRowBgAlt: 52>, 'TextLink': <Col.TextLink: 53>, 'TextSelectedBg': <Col.TextSelectedBg: 54>, 'DragDropTarget': <Col.DragDropTarget: 56>, 'NavHighlight': <Col.NavHighlight: 59>, 'NavWindowingHighlight': <Col.NavWindowingHighlight: 60>, 'NavWindowingDimBg': <Col.NavWindowingDimBg: 61>, 'ModalWindowDimBg': <Col.ModalWindowDimBg: 62>}
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
class ColorEditFlags:
    """
    Members:
    
      None
    
      NoAlpha
    
      NoPicker
    
      NoOptions
    
      NoSmallPreview
    
      NoInputs
    
      NoTooltip
    
      NoLabel
    
      NoSidePreview
    
      NoDragDrop
    
      NoBorder
    
      AlphaBar
    
      AlphaPreview
    
      AlphaPreviewHalf
    
      HDR
    
      DisplayRGB
    
      DisplayHSV
    
      DisplayHex
    
      Uint8
    
      Float
    
      PickerHueBar
    
      PickerHueWheel
    
      InputRGB
    
      InputHSV
    
      DefaultOptions
    
      DisplayMask
    
      DataTypeMask
    
      PickerMask
    
      InputMask
    """
    AlphaBar: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.AlphaBar: 262144>
    AlphaPreview: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.None: 0>
    AlphaPreviewHalf: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.AlphaPreviewHalf: 16384>
    DataTypeMask: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.DataTypeMask: 25165824>
    DefaultOptions: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.DefaultOptions: 311427072>
    DisplayHSV: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.DisplayHSV: 2097152>
    DisplayHex: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.DisplayHex: 4194304>
    DisplayMask: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.DisplayMask: 7340032>
    DisplayRGB: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.DisplayRGB: 1048576>
    Float: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.Float: 16777216>
    HDR: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.HDR: 524288>
    InputHSV: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.InputHSV: 536870912>
    InputMask: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.InputMask: 805306368>
    InputRGB: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.InputRGB: 268435456>
    NoAlpha: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoAlpha: 2>
    NoBorder: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoBorder: 1024>
    NoDragDrop: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoDragDrop: 512>
    NoInputs: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoInputs: 32>
    NoLabel: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoLabel: 128>
    NoOptions: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoOptions: 8>
    NoPicker: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoPicker: 4>
    NoSidePreview: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoSidePreview: 256>
    NoSmallPreview: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoSmallPreview: 16>
    NoTooltip: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.NoTooltip: 64>
    None: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.None: 0>
    PickerHueBar: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.PickerHueBar: 33554432>
    PickerHueWheel: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.PickerHueWheel: 67108864>
    PickerMask: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.PickerMask: 100663296>
    Uint8: typing.ClassVar[ColorEditFlags]  # value = <ColorEditFlags.Uint8: 8388608>
    __members__: typing.ClassVar[dict[str, ColorEditFlags]]  # value = {'None': <ColorEditFlags.None: 0>, 'NoAlpha': <ColorEditFlags.NoAlpha: 2>, 'NoPicker': <ColorEditFlags.NoPicker: 4>, 'NoOptions': <ColorEditFlags.NoOptions: 8>, 'NoSmallPreview': <ColorEditFlags.NoSmallPreview: 16>, 'NoInputs': <ColorEditFlags.NoInputs: 32>, 'NoTooltip': <ColorEditFlags.NoTooltip: 64>, 'NoLabel': <ColorEditFlags.NoLabel: 128>, 'NoSidePreview': <ColorEditFlags.NoSidePreview: 256>, 'NoDragDrop': <ColorEditFlags.NoDragDrop: 512>, 'NoBorder': <ColorEditFlags.NoBorder: 1024>, 'AlphaBar': <ColorEditFlags.AlphaBar: 262144>, 'AlphaPreview': <ColorEditFlags.None: 0>, 'AlphaPreviewHalf': <ColorEditFlags.AlphaPreviewHalf: 16384>, 'HDR': <ColorEditFlags.HDR: 524288>, 'DisplayRGB': <ColorEditFlags.DisplayRGB: 1048576>, 'DisplayHSV': <ColorEditFlags.DisplayHSV: 2097152>, 'DisplayHex': <ColorEditFlags.DisplayHex: 4194304>, 'Uint8': <ColorEditFlags.Uint8: 8388608>, 'Float': <ColorEditFlags.Float: 16777216>, 'PickerHueBar': <ColorEditFlags.PickerHueBar: 33554432>, 'PickerHueWheel': <ColorEditFlags.PickerHueWheel: 67108864>, 'InputRGB': <ColorEditFlags.InputRGB: 268435456>, 'InputHSV': <ColorEditFlags.InputHSV: 536870912>, 'DefaultOptions': <ColorEditFlags.DefaultOptions: 311427072>, 'DisplayMask': <ColorEditFlags.DisplayMask: 7340032>, 'DataTypeMask': <ColorEditFlags.DataTypeMask: 25165824>, 'PickerMask': <ColorEditFlags.PickerMask: 100663296>, 'InputMask': <ColorEditFlags.InputMask: 805306368>}
    @typing.overload
    def __eq__(self, other: ColorEditFlags) -> bool:
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
    def __ne__(self, other: ColorEditFlags) -> bool:
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
class ComboFlags:
    """
    Members:
    
      None
    
      PopupAlignLeft
    
      HeightSmall
    
      HeightRegular
    
      HeightLarge
    
      HeightLargest
    
      NoArrowButton
    
      NoPreview
    
      WidthFitPreview
    
      HeightMask
    """
    HeightLarge: typing.ClassVar[ComboFlags]  # value = <ComboFlags.HeightLarge: 8>
    HeightLargest: typing.ClassVar[ComboFlags]  # value = <ComboFlags.HeightLargest: 16>
    HeightMask: typing.ClassVar[ComboFlags]  # value = <ComboFlags.HeightMask: 30>
    HeightRegular: typing.ClassVar[ComboFlags]  # value = <ComboFlags.HeightRegular: 4>
    HeightSmall: typing.ClassVar[ComboFlags]  # value = <ComboFlags.HeightSmall: 2>
    NoArrowButton: typing.ClassVar[ComboFlags]  # value = <ComboFlags.NoArrowButton: 32>
    NoPreview: typing.ClassVar[ComboFlags]  # value = <ComboFlags.NoPreview: 64>
    None: typing.ClassVar[ComboFlags]  # value = <ComboFlags.None: 0>
    PopupAlignLeft: typing.ClassVar[ComboFlags]  # value = <ComboFlags.PopupAlignLeft: 1>
    WidthFitPreview: typing.ClassVar[ComboFlags]  # value = <ComboFlags.WidthFitPreview: 128>
    __members__: typing.ClassVar[dict[str, ComboFlags]]  # value = {'None': <ComboFlags.None: 0>, 'PopupAlignLeft': <ComboFlags.PopupAlignLeft: 1>, 'HeightSmall': <ComboFlags.HeightSmall: 2>, 'HeightRegular': <ComboFlags.HeightRegular: 4>, 'HeightLarge': <ComboFlags.HeightLarge: 8>, 'HeightLargest': <ComboFlags.HeightLargest: 16>, 'NoArrowButton': <ComboFlags.NoArrowButton: 32>, 'NoPreview': <ComboFlags.NoPreview: 64>, 'WidthFitPreview': <ComboFlags.WidthFitPreview: 128>, 'HeightMask': <ComboFlags.HeightMask: 30>}
    @typing.overload
    def __eq__(self, other: ComboFlags) -> bool:
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
    def __ne__(self, other: ComboFlags) -> bool:
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
    
      FirstUseEver
    
      Appearing
    """
    Always: typing.ClassVar[Cond]  # value = <Cond.Always: 1>
    Appearing: typing.ClassVar[Cond]  # value = <Cond.Appearing: 8>
    FirstUseEver: typing.ClassVar[Cond]  # value = <Cond.FirstUseEver: 4>
    None: typing.ClassVar[Cond]  # value = <Cond.None: 0>
    Once: typing.ClassVar[Cond]  # value = <Cond.Once: 2>
    __members__: typing.ClassVar[dict[str, Cond]]  # value = {'None': <Cond.None: 0>, 'Always': <Cond.Always: 1>, 'Once': <Cond.Once: 2>, 'FirstUseEver': <Cond.FirstUseEver: 4>, 'Appearing': <Cond.Appearing: 8>}
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
class ConfigFlags:
    """
    Members:
    
      None
    
      NavEnableKeyboard
    
      NavEnableGamepad
    
      NavEnableSetMousePos
    
      NavNoCaptureKeyboard
    
      NoMouse
    
      NoMouseCursorChange
    
      NoKeyboard
    
      DockingEnable
    
      ViewportsEnable
    
      DpiEnableScaleViewports
    
      DpiEnableScaleFonts
    
      IsSRGB
    
      IsTouchScreen
    """
    DockingEnable: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.DockingEnable: 128>
    DpiEnableScaleFonts: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.DpiEnableScaleFonts: 16384>
    DpiEnableScaleViewports: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.DpiEnableScaleViewports: 32768>
    IsSRGB: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.IsSRGB: 1048576>
    IsTouchScreen: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.IsTouchScreen: 2097152>
    NavEnableGamepad: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NavEnableGamepad: 2>
    NavEnableKeyboard: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NavEnableKeyboard: 1>
    NavEnableSetMousePos: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NavEnableSetMousePos: 4>
    NavNoCaptureKeyboard: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NavNoCaptureKeyboard: 8>
    NoKeyboard: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NoKeyboard: 64>
    NoMouse: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NoMouse: 16>
    NoMouseCursorChange: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.NoMouseCursorChange: 32>
    None: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.None: 0>
    ViewportsEnable: typing.ClassVar[ConfigFlags]  # value = <ConfigFlags.ViewportsEnable: 1024>
    __members__: typing.ClassVar[dict[str, ConfigFlags]]  # value = {'None': <ConfigFlags.None: 0>, 'NavEnableKeyboard': <ConfigFlags.NavEnableKeyboard: 1>, 'NavEnableGamepad': <ConfigFlags.NavEnableGamepad: 2>, 'NavEnableSetMousePos': <ConfigFlags.NavEnableSetMousePos: 4>, 'NavNoCaptureKeyboard': <ConfigFlags.NavNoCaptureKeyboard: 8>, 'NoMouse': <ConfigFlags.NoMouse: 16>, 'NoMouseCursorChange': <ConfigFlags.NoMouseCursorChange: 32>, 'NoKeyboard': <ConfigFlags.NoKeyboard: 64>, 'DockingEnable': <ConfigFlags.DockingEnable: 128>, 'ViewportsEnable': <ConfigFlags.ViewportsEnable: 1024>, 'DpiEnableScaleViewports': <ConfigFlags.DpiEnableScaleViewports: 32768>, 'DpiEnableScaleFonts': <ConfigFlags.DpiEnableScaleFonts: 16384>, 'IsSRGB': <ConfigFlags.IsSRGB: 1048576>, 'IsTouchScreen': <ConfigFlags.IsTouchScreen: 2097152>}
    @typing.overload
    def __eq__(self, other: ConfigFlags) -> bool:
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
    def __ne__(self, other: ConfigFlags) -> bool:
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
class DataType:
    """
    Members:
    
      S8
    
      U8
    
      S16
    
      U16
    
      S32
    
      U32
    
      S64
    
      U64
    
      Float
    
      Double
    """
    Double: typing.ClassVar[DataType]  # value = <DataType.Double: 9>
    Float: typing.ClassVar[DataType]  # value = <DataType.Float: 8>
    S16: typing.ClassVar[DataType]  # value = <DataType.S16: 2>
    S32: typing.ClassVar[DataType]  # value = <DataType.S32: 4>
    S64: typing.ClassVar[DataType]  # value = <DataType.S64: 6>
    S8: typing.ClassVar[DataType]  # value = <DataType.S8: 0>
    U16: typing.ClassVar[DataType]  # value = <DataType.U16: 3>
    U32: typing.ClassVar[DataType]  # value = <DataType.U32: 5>
    U64: typing.ClassVar[DataType]  # value = <DataType.U64: 7>
    U8: typing.ClassVar[DataType]  # value = <DataType.U8: 1>
    __members__: typing.ClassVar[dict[str, DataType]]  # value = {'S8': <DataType.S8: 0>, 'U8': <DataType.U8: 1>, 'S16': <DataType.S16: 2>, 'U16': <DataType.U16: 3>, 'S32': <DataType.S32: 4>, 'U32': <DataType.U32: 5>, 'S64': <DataType.S64: 6>, 'U64': <DataType.U64: 7>, 'Float': <DataType.Float: 8>, 'Double': <DataType.Double: 9>}
    @typing.overload
    def __eq__(self, other: DataType) -> bool:
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
    def __ne__(self, other: DataType) -> bool:
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
class Dir:
    """
    Members:
    
      None
    
      Left
    
      Right
    
      Up
    
      Down
    """
    Down: typing.ClassVar[Dir]  # value = <Dir.Down: 3>
    Left: typing.ClassVar[Dir]  # value = <Dir.Left: 0>
    None: typing.ClassVar[Dir]  # value = <Dir.None: -1>
    Right: typing.ClassVar[Dir]  # value = <Dir.Right: 1>
    Up: typing.ClassVar[Dir]  # value = <Dir.Up: 2>
    __members__: typing.ClassVar[dict[str, Dir]]  # value = {'None': <Dir.None: -1>, 'Left': <Dir.Left: 0>, 'Right': <Dir.Right: 1>, 'Up': <Dir.Up: 2>, 'Down': <Dir.Down: 3>}
    @typing.overload
    def __eq__(self, other: Dir) -> bool:
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
    def __ne__(self, other: Dir) -> bool:
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
class DockNodeFlags:
    """
    Members:
    
      None
    
      KeepAliveOnly
    
      NoDockingOverCentralNode
    
      PassthruCentralNode
    
      NoDockingSplit
    
      NoResize
    
      AutoHideTabBar
    
      NoUndocking
    """
    AutoHideTabBar: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.AutoHideTabBar: 64>
    KeepAliveOnly: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.KeepAliveOnly: 1>
    NoDockingOverCentralNode: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.NoDockingOverCentralNode: 4>
    NoDockingSplit: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.NoDockingSplit: 16>
    NoResize: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.NoResize: 32>
    NoUndocking: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.NoUndocking: 128>
    None: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.None: 0>
    PassthruCentralNode: typing.ClassVar[DockNodeFlags]  # value = <DockNodeFlags.PassthruCentralNode: 8>
    __members__: typing.ClassVar[dict[str, DockNodeFlags]]  # value = {'None': <DockNodeFlags.None: 0>, 'KeepAliveOnly': <DockNodeFlags.KeepAliveOnly: 1>, 'NoDockingOverCentralNode': <DockNodeFlags.NoDockingOverCentralNode: 4>, 'PassthruCentralNode': <DockNodeFlags.PassthruCentralNode: 8>, 'NoDockingSplit': <DockNodeFlags.NoDockingSplit: 16>, 'NoResize': <DockNodeFlags.NoResize: 32>, 'AutoHideTabBar': <DockNodeFlags.AutoHideTabBar: 64>, 'NoUndocking': <DockNodeFlags.NoUndocking: 128>}
    @typing.overload
    def __eq__(self, other: DockNodeFlags) -> bool:
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
    def __ne__(self, other: DockNodeFlags) -> bool:
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
class DragDropFlags:
    """
    Members:
    
      None
    
      SourceNoPreviewTooltip
    
      SourceNoDisableHover
    
      SourceNoHoldToOpenOthers
    
      SourceAllowNullID
    
      SourceExtern
    
      PayloadAutoExpire
    
      PayloadNoCrossContext
    
      PayloadNoCrossProcess
    
      AcceptBeforeDelivery
    
      AcceptNoDrawDefaultRect
    
      AcceptNoPreviewTooltip
    
      AcceptPeekOnly
    """
    AcceptBeforeDelivery: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.AcceptBeforeDelivery: 1024>
    AcceptNoDrawDefaultRect: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.AcceptNoDrawDefaultRect: 2048>
    AcceptNoPreviewTooltip: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.AcceptNoPreviewTooltip: 4096>
    AcceptPeekOnly: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.AcceptPeekOnly: 3072>
    None: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.None: 0>
    PayloadAutoExpire: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.PayloadAutoExpire: 32>
    PayloadNoCrossContext: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.PayloadNoCrossContext: 64>
    PayloadNoCrossProcess: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.PayloadNoCrossProcess: 128>
    SourceAllowNullID: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.SourceAllowNullID: 8>
    SourceExtern: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.SourceExtern: 16>
    SourceNoDisableHover: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.SourceNoDisableHover: 2>
    SourceNoHoldToOpenOthers: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.SourceNoHoldToOpenOthers: 4>
    SourceNoPreviewTooltip: typing.ClassVar[DragDropFlags]  # value = <DragDropFlags.SourceNoPreviewTooltip: 1>
    __members__: typing.ClassVar[dict[str, DragDropFlags]]  # value = {'None': <DragDropFlags.None: 0>, 'SourceNoPreviewTooltip': <DragDropFlags.SourceNoPreviewTooltip: 1>, 'SourceNoDisableHover': <DragDropFlags.SourceNoDisableHover: 2>, 'SourceNoHoldToOpenOthers': <DragDropFlags.SourceNoHoldToOpenOthers: 4>, 'SourceAllowNullID': <DragDropFlags.SourceAllowNullID: 8>, 'SourceExtern': <DragDropFlags.SourceExtern: 16>, 'PayloadAutoExpire': <DragDropFlags.PayloadAutoExpire: 32>, 'PayloadNoCrossContext': <DragDropFlags.PayloadNoCrossContext: 64>, 'PayloadNoCrossProcess': <DragDropFlags.PayloadNoCrossProcess: 128>, 'AcceptBeforeDelivery': <DragDropFlags.AcceptBeforeDelivery: 1024>, 'AcceptNoDrawDefaultRect': <DragDropFlags.AcceptNoDrawDefaultRect: 2048>, 'AcceptNoPreviewTooltip': <DragDropFlags.AcceptNoPreviewTooltip: 4096>, 'AcceptPeekOnly': <DragDropFlags.AcceptPeekOnly: 3072>}
    @typing.overload
    def __eq__(self, other: DragDropFlags) -> bool:
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
    def __ne__(self, other: DragDropFlags) -> bool:
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
class DrawFlags:
    """
    Members:
    
      None
    
      Closed
    
      RoundCornersTopLeft
    
      RoundCornersTopRight
    
      RoundCornersBottomLeft
    
      RoundCornersBottomRight
    
      RoundCornersNone
    
      RoundCornersTop
    
      RoundCornersBottom
    
      RoundCornersLeft
    
      RoundCornersRight
    
      RoundCornersAll
    """
    Closed: typing.ClassVar[DrawFlags]  # value = <DrawFlags.Closed: 512>
    None: typing.ClassVar[DrawFlags]  # value = <DrawFlags.None: 0>
    RoundCornersAll: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersAll: 240>
    RoundCornersBottom: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersBottom: 192>
    RoundCornersBottomLeft: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersBottomLeft: 64>
    RoundCornersBottomRight: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersBottomRight: 128>
    RoundCornersLeft: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersLeft: 80>
    RoundCornersNone: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersNone: 256>
    RoundCornersRight: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersRight: 160>
    RoundCornersTop: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersTop: 48>
    RoundCornersTopLeft: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersTopLeft: 16>
    RoundCornersTopRight: typing.ClassVar[DrawFlags]  # value = <DrawFlags.RoundCornersTopRight: 32>
    __members__: typing.ClassVar[dict[str, DrawFlags]]  # value = {'None': <DrawFlags.None: 0>, 'Closed': <DrawFlags.Closed: 512>, 'RoundCornersTopLeft': <DrawFlags.RoundCornersTopLeft: 16>, 'RoundCornersTopRight': <DrawFlags.RoundCornersTopRight: 32>, 'RoundCornersBottomLeft': <DrawFlags.RoundCornersBottomLeft: 64>, 'RoundCornersBottomRight': <DrawFlags.RoundCornersBottomRight: 128>, 'RoundCornersNone': <DrawFlags.RoundCornersNone: 256>, 'RoundCornersTop': <DrawFlags.RoundCornersTop: 48>, 'RoundCornersBottom': <DrawFlags.RoundCornersBottom: 192>, 'RoundCornersLeft': <DrawFlags.RoundCornersLeft: 80>, 'RoundCornersRight': <DrawFlags.RoundCornersRight: 160>, 'RoundCornersAll': <DrawFlags.RoundCornersAll: 240>}
    @typing.overload
    def __eq__(self, other: DrawFlags) -> bool:
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
    def __ne__(self, other: DrawFlags) -> bool:
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
class DrawList:
    def AddCircle(self, center: Vec2, radius: typing.SupportsFloat | typing.SupportsIndex, col: typing.SupportsInt | typing.SupportsIndex, num_segments: typing.SupportsInt | typing.SupportsIndex = 0, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> None:
        ...
    def AddCircleFilled(self, center: Vec2, radius: typing.SupportsFloat | typing.SupportsIndex, col: typing.SupportsInt | typing.SupportsIndex, num_segments: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        ...
    def AddConvexPolyFilled(self, points: collections.abc.Sequence[Vec2], col: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def AddLine(self, p1: Vec2, p2: Vec2, col: typing.SupportsInt | typing.SupportsIndex, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> None:
        ...
    def AddPolyline(self, points: collections.abc.Sequence[Vec2], col: typing.SupportsInt | typing.SupportsIndex, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        ...
    def AddRect(self, p_min: Vec2, p_max: Vec2, col: typing.SupportsInt | typing.SupportsIndex, rounding: typing.SupportsFloat | typing.SupportsIndex = 0.0, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        ...
    def AddRectFilled(self, p_min: Vec2, p_max: Vec2, col: typing.SupportsInt | typing.SupportsIndex, rounding: typing.SupportsFloat | typing.SupportsIndex = 0.0, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        ...
    def AddText(self, pos: Vec2, col: typing.SupportsInt | typing.SupportsIndex, text: str) -> None:
        ...
    def AddTriangle(self, p1: Vec2, p2: Vec2, p3: Vec2, col: typing.SupportsInt | typing.SupportsIndex, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> None:
        ...
    def AddTriangleFilled(self, p1: Vec2, p2: Vec2, p3: Vec2, col: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def PathArcTo(self, center: Vec2, radius: typing.SupportsFloat | typing.SupportsIndex, a_min: typing.SupportsFloat | typing.SupportsIndex, a_max: typing.SupportsFloat | typing.SupportsIndex, num_segments: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        ...
    def PathClear(self) -> None:
        ...
    def PathFillConvex(self, col: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def PathLineTo(self, pos: Vec2) -> None:
        ...
    def PathStroke(self, col: typing.SupportsInt | typing.SupportsIndex, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
        ...
class FocusedFlags:
    """
    Members:
    
      None
    
      ChildWindows
    
      RootWindow
    
      AnyWindow
    
      NoPopupHierarchy
    
      DockHierarchy
    
      RootAndChildWindows
    """
    AnyWindow: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.AnyWindow: 4>
    ChildWindows: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.ChildWindows: 1>
    DockHierarchy: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.DockHierarchy: 16>
    NoPopupHierarchy: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.NoPopupHierarchy: 8>
    None: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.None: 0>
    RootAndChildWindows: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.RootAndChildWindows: 3>
    RootWindow: typing.ClassVar[FocusedFlags]  # value = <FocusedFlags.RootWindow: 2>
    __members__: typing.ClassVar[dict[str, FocusedFlags]]  # value = {'None': <FocusedFlags.None: 0>, 'ChildWindows': <FocusedFlags.ChildWindows: 1>, 'RootWindow': <FocusedFlags.RootWindow: 2>, 'AnyWindow': <FocusedFlags.AnyWindow: 4>, 'NoPopupHierarchy': <FocusedFlags.NoPopupHierarchy: 8>, 'DockHierarchy': <FocusedFlags.DockHierarchy: 16>, 'RootAndChildWindows': <FocusedFlags.RootAndChildWindows: 3>}
    @typing.overload
    def __eq__(self, other: FocusedFlags) -> bool:
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
    def __ne__(self, other: FocusedFlags) -> bool:
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
class Font:
    pass
class FontAtlas:
    def __getitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> ImFont:
        ...
    def __len__(self) -> int:
        ...
class HoveredFlags:
    """
    Members:
    
      None
    
      ChildWindows
    
      RootWindow
    
      AnyWindow
    
      NoPopupHierarchy
    
      DockHierarchy
    
      AllowWhenBlockedByPopup
    
      AllowWhenBlockedByActiveItem
    
      AllowWhenOverlappedByItem
    
      AllowWhenOverlappedByWindow
    
      AllowWhenDisabled
    
      NoNavOverride
    
      AllowWhenOverlapped
    
      RectOnly
    
      RootAndChildWindows
    
      ForTooltip
    
      Stationary
    
      DelayNone
    
      DelayShort
    
      DelayNormal
    
      NoSharedDelay
    """
    AllowWhenBlockedByActiveItem: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AllowWhenBlockedByActiveItem: 128>
    AllowWhenBlockedByPopup: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AllowWhenBlockedByPopup: 32>
    AllowWhenDisabled: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AllowWhenDisabled: 1024>
    AllowWhenOverlapped: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AllowWhenOverlapped: 768>
    AllowWhenOverlappedByItem: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AllowWhenOverlappedByItem: 256>
    AllowWhenOverlappedByWindow: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AllowWhenOverlappedByWindow: 512>
    AnyWindow: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.AnyWindow: 4>
    ChildWindows: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.ChildWindows: 1>
    DelayNone: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.DelayNone: 16384>
    DelayNormal: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.DelayNormal: 65536>
    DelayShort: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.DelayShort: 32768>
    DockHierarchy: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.DockHierarchy: 16>
    ForTooltip: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.ForTooltip: 4096>
    NoNavOverride: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.NoNavOverride: 2048>
    NoPopupHierarchy: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.NoPopupHierarchy: 8>
    NoSharedDelay: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.NoSharedDelay: 131072>
    None: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.None: 0>
    RectOnly: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.RectOnly: 928>
    RootAndChildWindows: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.RootAndChildWindows: 3>
    RootWindow: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.RootWindow: 2>
    Stationary: typing.ClassVar[HoveredFlags]  # value = <HoveredFlags.Stationary: 8192>
    __members__: typing.ClassVar[dict[str, HoveredFlags]]  # value = {'None': <HoveredFlags.None: 0>, 'ChildWindows': <HoveredFlags.ChildWindows: 1>, 'RootWindow': <HoveredFlags.RootWindow: 2>, 'AnyWindow': <HoveredFlags.AnyWindow: 4>, 'NoPopupHierarchy': <HoveredFlags.NoPopupHierarchy: 8>, 'DockHierarchy': <HoveredFlags.DockHierarchy: 16>, 'AllowWhenBlockedByPopup': <HoveredFlags.AllowWhenBlockedByPopup: 32>, 'AllowWhenBlockedByActiveItem': <HoveredFlags.AllowWhenBlockedByActiveItem: 128>, 'AllowWhenOverlappedByItem': <HoveredFlags.AllowWhenOverlappedByItem: 256>, 'AllowWhenOverlappedByWindow': <HoveredFlags.AllowWhenOverlappedByWindow: 512>, 'AllowWhenDisabled': <HoveredFlags.AllowWhenDisabled: 1024>, 'NoNavOverride': <HoveredFlags.NoNavOverride: 2048>, 'AllowWhenOverlapped': <HoveredFlags.AllowWhenOverlapped: 768>, 'RectOnly': <HoveredFlags.RectOnly: 928>, 'RootAndChildWindows': <HoveredFlags.RootAndChildWindows: 3>, 'ForTooltip': <HoveredFlags.ForTooltip: 4096>, 'Stationary': <HoveredFlags.Stationary: 8192>, 'DelayNone': <HoveredFlags.DelayNone: 16384>, 'DelayShort': <HoveredFlags.DelayShort: 32768>, 'DelayNormal': <HoveredFlags.DelayNormal: 65536>, 'NoSharedDelay': <HoveredFlags.NoSharedDelay: 131072>}
    @typing.overload
    def __eq__(self, other: HoveredFlags) -> bool:
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
    def __ne__(self, other: HoveredFlags) -> bool:
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
class IO:
    ConfigErrorRecoveryEnableAssert: bool
    ConfigErrorRecoveryEnableDebugLog: bool
    ConfigErrorRecoveryEnableTooltip: bool
    DisplaySize: Vec2
    WantSaveIniSettings: bool
    @property
    def BackendFlags(self) -> int:
        ...
    @BackendFlags.setter
    def BackendFlags(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def ConfigFlags(self) -> int:
        ...
    @ConfigFlags.setter
    def ConfigFlags(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def DeltaTime(self) -> float:
        ...
    @property
    def FontGlobalScale(self) -> float:
        ...
    @property
    def Fonts(self) -> ImFontAtlas:
        ...
    @property
    def Framerate(self) -> float:
        ...
    @property
    def KeyAlt(self) -> bool:
        ...
    @property
    def KeyCtrl(self) -> bool:
        ...
    @property
    def KeyShift(self) -> bool:
        ...
    @property
    def KeySuper(self) -> bool:
        ...
    @property
    def MouseDelta(self) -> Vec2:
        ...
    @property
    def MousePos(self) -> Vec2:
        ...
    @property
    def MouseWheel(self) -> float:
        ...
    @property
    def WantCaptureKeyboard(self) -> bool:
        ...
    @property
    def WantCaptureMouse(self) -> bool:
        ...
class InputFlags:
    """
    Members:
    
      None
    
      Repeat
    
      RouteActive
    
      RouteFocused
    
      RouteGlobal
    
      RouteAlways
    
      RouteOverFocused
    
      RouteOverActive
    
      RouteUnlessBgFocused
    
      RouteFromRootWindow
    
      Tooltip
    """
    None: typing.ClassVar[InputFlags]  # value = <InputFlags.None: 0>
    Repeat: typing.ClassVar[InputFlags]  # value = <InputFlags.Repeat: 1>
    RouteActive: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteActive: 1024>
    RouteAlways: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteAlways: 8192>
    RouteFocused: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteFocused: 2048>
    RouteFromRootWindow: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteFromRootWindow: 131072>
    RouteGlobal: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteGlobal: 4096>
    RouteOverActive: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteOverActive: 32768>
    RouteOverFocused: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteOverFocused: 16384>
    RouteUnlessBgFocused: typing.ClassVar[InputFlags]  # value = <InputFlags.RouteUnlessBgFocused: 65536>
    Tooltip: typing.ClassVar[InputFlags]  # value = <InputFlags.Tooltip: 262144>
    __members__: typing.ClassVar[dict[str, InputFlags]]  # value = {'None': <InputFlags.None: 0>, 'Repeat': <InputFlags.Repeat: 1>, 'RouteActive': <InputFlags.RouteActive: 1024>, 'RouteFocused': <InputFlags.RouteFocused: 2048>, 'RouteGlobal': <InputFlags.RouteGlobal: 4096>, 'RouteAlways': <InputFlags.RouteAlways: 8192>, 'RouteOverFocused': <InputFlags.RouteOverFocused: 16384>, 'RouteOverActive': <InputFlags.RouteOverActive: 32768>, 'RouteUnlessBgFocused': <InputFlags.RouteUnlessBgFocused: 65536>, 'RouteFromRootWindow': <InputFlags.RouteFromRootWindow: 131072>, 'Tooltip': <InputFlags.Tooltip: 262144>}
    @typing.overload
    def __eq__(self, other: InputFlags) -> bool:
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
    def __ne__(self, other: InputFlags) -> bool:
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
class InputTextFlags:
    """
    Members:
    
      None
    
      CharsDecimal
    
      CharsHexadecimal
    
      CharsScientific
    
      CharsUppercase
    
      CharsNoBlank
    
      AllowTabInput
    
      EnterReturnsTrue
    
      EscapeClearsAll
    
      CtrlEnterForNewLine
    
      ReadOnly
    
      Password
    
      AlwaysOverwrite
    
      AutoSelectAll
    
      ParseEmptyRefVal
    
      DisplayEmptyRefVal
    
      NoHorizontalScroll
    
      NoUndoRedo
    
      CallbackCompletion
    
      CallbackHistory
    
      CallbackAlways
    
      CallbackCharFilter
    
      CallbackResize
    
      CallbackEdit
    
      WordWrap
    """
    AllowTabInput: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.AllowTabInput: 32>
    AlwaysOverwrite: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.AlwaysOverwrite: 2048>
    AutoSelectAll: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.AutoSelectAll: 4096>
    CallbackAlways: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CallbackAlways: 1048576>
    CallbackCharFilter: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CallbackCharFilter: 2097152>
    CallbackCompletion: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CallbackCompletion: 262144>
    CallbackEdit: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CallbackEdit: 8388608>
    CallbackHistory: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CallbackHistory: 524288>
    CallbackResize: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CallbackResize: 4194304>
    CharsDecimal: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CharsDecimal: 1>
    CharsHexadecimal: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CharsHexadecimal: 2>
    CharsNoBlank: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CharsNoBlank: 16>
    CharsScientific: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CharsScientific: 4>
    CharsUppercase: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CharsUppercase: 8>
    CtrlEnterForNewLine: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.CtrlEnterForNewLine: 256>
    DisplayEmptyRefVal: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.DisplayEmptyRefVal: 16384>
    EnterReturnsTrue: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.EnterReturnsTrue: 64>
    EscapeClearsAll: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.EscapeClearsAll: 128>
    NoHorizontalScroll: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.NoHorizontalScroll: 32768>
    NoUndoRedo: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.NoUndoRedo: 65536>
    None: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.None: 0>
    ParseEmptyRefVal: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.ParseEmptyRefVal: 8192>
    Password: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.Password: 1024>
    ReadOnly: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.ReadOnly: 512>
    WordWrap: typing.ClassVar[InputTextFlags]  # value = <InputTextFlags.WordWrap: 16777216>
    __members__: typing.ClassVar[dict[str, InputTextFlags]]  # value = {'None': <InputTextFlags.None: 0>, 'CharsDecimal': <InputTextFlags.CharsDecimal: 1>, 'CharsHexadecimal': <InputTextFlags.CharsHexadecimal: 2>, 'CharsScientific': <InputTextFlags.CharsScientific: 4>, 'CharsUppercase': <InputTextFlags.CharsUppercase: 8>, 'CharsNoBlank': <InputTextFlags.CharsNoBlank: 16>, 'AllowTabInput': <InputTextFlags.AllowTabInput: 32>, 'EnterReturnsTrue': <InputTextFlags.EnterReturnsTrue: 64>, 'EscapeClearsAll': <InputTextFlags.EscapeClearsAll: 128>, 'CtrlEnterForNewLine': <InputTextFlags.CtrlEnterForNewLine: 256>, 'ReadOnly': <InputTextFlags.ReadOnly: 512>, 'Password': <InputTextFlags.Password: 1024>, 'AlwaysOverwrite': <InputTextFlags.AlwaysOverwrite: 2048>, 'AutoSelectAll': <InputTextFlags.AutoSelectAll: 4096>, 'ParseEmptyRefVal': <InputTextFlags.ParseEmptyRefVal: 8192>, 'DisplayEmptyRefVal': <InputTextFlags.DisplayEmptyRefVal: 16384>, 'NoHorizontalScroll': <InputTextFlags.NoHorizontalScroll: 32768>, 'NoUndoRedo': <InputTextFlags.NoUndoRedo: 65536>, 'CallbackCompletion': <InputTextFlags.CallbackCompletion: 262144>, 'CallbackHistory': <InputTextFlags.CallbackHistory: 524288>, 'CallbackAlways': <InputTextFlags.CallbackAlways: 1048576>, 'CallbackCharFilter': <InputTextFlags.CallbackCharFilter: 2097152>, 'CallbackResize': <InputTextFlags.CallbackResize: 4194304>, 'CallbackEdit': <InputTextFlags.CallbackEdit: 8388608>, 'WordWrap': <InputTextFlags.WordWrap: 16777216>}
    @typing.overload
    def __eq__(self, other: InputTextFlags) -> bool:
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
    def __ne__(self, other: InputTextFlags) -> bool:
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
class Key:
    """
    Members:
    
      None
    
      Tab
    
      LeftArrow
    
      RightArrow
    
      UpArrow
    
      DownArrow
    
      PageUp
    
      PageDown
    
      Home
    
      End
    
      Insert
    
      Delete
    
      Backspace
    
      Space
    
      Enter
    
      Escape
    
      LeftCtrl
    
      LeftShift
    
      LeftAlt
    
      LeftSuper
    
      RightCtrl
    
      RightShift
    
      RightAlt
    
      RightSuper
    
      Menu
    
      N0
    
      N1
    
      N2
    
      N3
    
      N4
    
      N5
    
      N6
    
      N7
    
      N8
    
      N9
    
      A
    
      B
    
      C
    
      D
    
      E
    
      F
    
      G
    
      H
    
      I
    
      J
    
      K
    
      L
    
      M
    
      N
    
      O
    
      P
    
      Q
    
      R
    
      S
    
      T
    
      U
    
      V
    
      W
    
      X
    
      Y
    
      Z
    
      F1
    
      F2
    
      F3
    
      F4
    
      F5
    
      F6
    
      F7
    
      F8
    
      F9
    
      F10
    
      F11
    
      F12
    
      F13
    
      F14
    
      F15
    
      F16
    
      F17
    
      F18
    
      F19
    
      F20
    
      F21
    
      F22
    
      F23
    
      F24
    
      Apostrophe
    
      Comma
    
      Minus
    
      Period
    
      Slash
    
      Semicolon
    
      Equal
    
      LeftBracket
    
      Backslash
    
      RightBracket
    
      GraveAccent
    
      CapsLock
    
      ScrollLock
    
      NumLock
    
      PrintScreen
    
      Pause
    
      Keypad0
    
      Keypad1
    
      Keypad2
    
      Keypad3
    
      Keypad4
    
      Keypad5
    
      Keypad6
    
      Keypad7
    
      Keypad8
    
      Keypad9
    
      KeypadDecimal
    
      KeypadDivide
    
      KeypadMultiply
    
      KeypadSubtract
    
      KeypadAdd
    
      KeypadEnter
    
      KeypadEqual
    
      AppBack
    
      AppForward
    
      GamepadStart
    
      GamepadBack
    
      GamepadFaceLeft
    
      GamepadFaceRight
    
      GamepadFaceUp
    
      GamepadFaceDown
    
      GamepadDpadLeft
    
      GamepadDpadRight
    
      GamepadDpadUp
    
      GamepadDpadDown
    
      GamepadL1
    
      GamepadR1
    
      GamepadL2
    
      GamepadR2
    
      GamepadL3
    
      GamepadR3
    
      GamepadLStickLeft
    
      GamepadLStickRight
    
      GamepadLStickUp
    
      GamepadLStickDown
    
      GamepadRStickLeft
    
      GamepadRStickRight
    
      GamepadRStickUp
    
      GamepadRStickDown
    
      MouseLeft
    
      MouseRight
    
      MouseMiddle
    
      MouseX1
    
      MouseX2
    
      MouseWheelX
    
      MouseWheelY
    
      ReservedForModCtrl
    
      ReservedForModShift
    
      ReservedForModAlt
    
      ReservedForModSuper
    
      Ctrl
    
      Shift
    
      Alt
    
      Super
    
      Mask
    """
    A: typing.ClassVar[Key]  # value = <Key.A: 546>
    Alt: typing.ClassVar[Key]  # value = <Key.Alt: 16384>
    Apostrophe: typing.ClassVar[Key]  # value = <Key.Apostrophe: 596>
    AppBack: typing.ClassVar[Key]  # value = <Key.AppBack: 629>
    AppForward: typing.ClassVar[Key]  # value = <Key.AppForward: 630>
    B: typing.ClassVar[Key]  # value = <Key.B: 547>
    Backslash: typing.ClassVar[Key]  # value = <Key.Backslash: 604>
    Backspace: typing.ClassVar[Key]  # value = <Key.Backspace: 523>
    C: typing.ClassVar[Key]  # value = <Key.C: 548>
    CapsLock: typing.ClassVar[Key]  # value = <Key.CapsLock: 607>
    Comma: typing.ClassVar[Key]  # value = <Key.Comma: 597>
    Ctrl: typing.ClassVar[Key]  # value = <Key.Ctrl: 4096>
    D: typing.ClassVar[Key]  # value = <Key.D: 549>
    Delete: typing.ClassVar[Key]  # value = <Key.Delete: 522>
    DownArrow: typing.ClassVar[Key]  # value = <Key.DownArrow: 516>
    E: typing.ClassVar[Key]  # value = <Key.E: 550>
    End: typing.ClassVar[Key]  # value = <Key.End: 520>
    Enter: typing.ClassVar[Key]  # value = <Key.Enter: 525>
    Equal: typing.ClassVar[Key]  # value = <Key.Equal: 602>
    Escape: typing.ClassVar[Key]  # value = <Key.Escape: 526>
    F: typing.ClassVar[Key]  # value = <Key.F: 551>
    F1: typing.ClassVar[Key]  # value = <Key.F1: 572>
    F10: typing.ClassVar[Key]  # value = <Key.F10: 581>
    F11: typing.ClassVar[Key]  # value = <Key.F11: 582>
    F12: typing.ClassVar[Key]  # value = <Key.F12: 583>
    F13: typing.ClassVar[Key]  # value = <Key.F13: 584>
    F14: typing.ClassVar[Key]  # value = <Key.F14: 585>
    F15: typing.ClassVar[Key]  # value = <Key.F15: 586>
    F16: typing.ClassVar[Key]  # value = <Key.F16: 587>
    F17: typing.ClassVar[Key]  # value = <Key.F17: 588>
    F18: typing.ClassVar[Key]  # value = <Key.F18: 589>
    F19: typing.ClassVar[Key]  # value = <Key.F19: 590>
    F2: typing.ClassVar[Key]  # value = <Key.F2: 573>
    F20: typing.ClassVar[Key]  # value = <Key.F20: 591>
    F21: typing.ClassVar[Key]  # value = <Key.F21: 592>
    F22: typing.ClassVar[Key]  # value = <Key.F22: 593>
    F23: typing.ClassVar[Key]  # value = <Key.F23: 594>
    F24: typing.ClassVar[Key]  # value = <Key.F24: 595>
    F3: typing.ClassVar[Key]  # value = <Key.F3: 574>
    F4: typing.ClassVar[Key]  # value = <Key.F4: 575>
    F5: typing.ClassVar[Key]  # value = <Key.F5: 576>
    F6: typing.ClassVar[Key]  # value = <Key.F6: 577>
    F7: typing.ClassVar[Key]  # value = <Key.F7: 578>
    F8: typing.ClassVar[Key]  # value = <Key.F8: 579>
    F9: typing.ClassVar[Key]  # value = <Key.F9: 580>
    G: typing.ClassVar[Key]  # value = <Key.G: 552>
    GamepadBack: typing.ClassVar[Key]  # value = <Key.GamepadBack: 633>
    GamepadDpadDown: typing.ClassVar[Key]  # value = <Key.GamepadDpadDown: 641>
    GamepadDpadLeft: typing.ClassVar[Key]  # value = <Key.GamepadDpadLeft: 638>
    GamepadDpadRight: typing.ClassVar[Key]  # value = <Key.GamepadDpadRight: 639>
    GamepadDpadUp: typing.ClassVar[Key]  # value = <Key.GamepadDpadUp: 640>
    GamepadFaceDown: typing.ClassVar[Key]  # value = <Key.GamepadFaceDown: 637>
    GamepadFaceLeft: typing.ClassVar[Key]  # value = <Key.GamepadFaceLeft: 634>
    GamepadFaceRight: typing.ClassVar[Key]  # value = <Key.GamepadFaceRight: 635>
    GamepadFaceUp: typing.ClassVar[Key]  # value = <Key.GamepadFaceUp: 636>
    GamepadL1: typing.ClassVar[Key]  # value = <Key.GamepadL1: 642>
    GamepadL2: typing.ClassVar[Key]  # value = <Key.GamepadL2: 644>
    GamepadL3: typing.ClassVar[Key]  # value = <Key.GamepadL3: 646>
    GamepadLStickDown: typing.ClassVar[Key]  # value = <Key.GamepadLStickDown: 651>
    GamepadLStickLeft: typing.ClassVar[Key]  # value = <Key.GamepadLStickLeft: 648>
    GamepadLStickRight: typing.ClassVar[Key]  # value = <Key.GamepadLStickRight: 649>
    GamepadLStickUp: typing.ClassVar[Key]  # value = <Key.GamepadLStickUp: 650>
    GamepadR1: typing.ClassVar[Key]  # value = <Key.GamepadR1: 643>
    GamepadR2: typing.ClassVar[Key]  # value = <Key.GamepadR2: 645>
    GamepadR3: typing.ClassVar[Key]  # value = <Key.GamepadR3: 647>
    GamepadRStickDown: typing.ClassVar[Key]  # value = <Key.GamepadRStickDown: 655>
    GamepadRStickLeft: typing.ClassVar[Key]  # value = <Key.GamepadRStickLeft: 652>
    GamepadRStickRight: typing.ClassVar[Key]  # value = <Key.GamepadRStickRight: 653>
    GamepadRStickUp: typing.ClassVar[Key]  # value = <Key.GamepadRStickUp: 654>
    GamepadStart: typing.ClassVar[Key]  # value = <Key.GamepadStart: 632>
    GraveAccent: typing.ClassVar[Key]  # value = <Key.GraveAccent: 606>
    H: typing.ClassVar[Key]  # value = <Key.H: 553>
    Home: typing.ClassVar[Key]  # value = <Key.Home: 519>
    I: typing.ClassVar[Key]  # value = <Key.I: 554>
    Insert: typing.ClassVar[Key]  # value = <Key.Insert: 521>
    J: typing.ClassVar[Key]  # value = <Key.J: 555>
    K: typing.ClassVar[Key]  # value = <Key.K: 556>
    Keypad0: typing.ClassVar[Key]  # value = <Key.Keypad0: 612>
    Keypad1: typing.ClassVar[Key]  # value = <Key.Keypad1: 613>
    Keypad2: typing.ClassVar[Key]  # value = <Key.Keypad2: 614>
    Keypad3: typing.ClassVar[Key]  # value = <Key.Keypad3: 615>
    Keypad4: typing.ClassVar[Key]  # value = <Key.Keypad4: 616>
    Keypad5: typing.ClassVar[Key]  # value = <Key.Keypad5: 617>
    Keypad6: typing.ClassVar[Key]  # value = <Key.Keypad6: 618>
    Keypad7: typing.ClassVar[Key]  # value = <Key.Keypad7: 619>
    Keypad8: typing.ClassVar[Key]  # value = <Key.Keypad8: 620>
    Keypad9: typing.ClassVar[Key]  # value = <Key.Keypad9: 621>
    KeypadAdd: typing.ClassVar[Key]  # value = <Key.KeypadAdd: 626>
    KeypadDecimal: typing.ClassVar[Key]  # value = <Key.KeypadDecimal: 622>
    KeypadDivide: typing.ClassVar[Key]  # value = <Key.KeypadDivide: 623>
    KeypadEnter: typing.ClassVar[Key]  # value = <Key.KeypadEnter: 627>
    KeypadEqual: typing.ClassVar[Key]  # value = <Key.KeypadEqual: 628>
    KeypadMultiply: typing.ClassVar[Key]  # value = <Key.KeypadMultiply: 624>
    KeypadSubtract: typing.ClassVar[Key]  # value = <Key.KeypadSubtract: 625>
    L: typing.ClassVar[Key]  # value = <Key.L: 557>
    LeftAlt: typing.ClassVar[Key]  # value = <Key.LeftAlt: 529>
    LeftArrow: typing.ClassVar[Key]  # value = <Key.LeftArrow: 513>
    LeftBracket: typing.ClassVar[Key]  # value = <Key.LeftBracket: 603>
    LeftCtrl: typing.ClassVar[Key]  # value = <Key.LeftCtrl: 527>
    LeftShift: typing.ClassVar[Key]  # value = <Key.LeftShift: 528>
    LeftSuper: typing.ClassVar[Key]  # value = <Key.LeftSuper: 530>
    M: typing.ClassVar[Key]  # value = <Key.M: 558>
    Mask: typing.ClassVar[Key]  # value = <Key.Mask: 61440>
    Menu: typing.ClassVar[Key]  # value = <Key.Menu: 535>
    Minus: typing.ClassVar[Key]  # value = <Key.Minus: 598>
    MouseLeft: typing.ClassVar[Key]  # value = <Key.MouseLeft: 656>
    MouseMiddle: typing.ClassVar[Key]  # value = <Key.MouseMiddle: 658>
    MouseRight: typing.ClassVar[Key]  # value = <Key.MouseRight: 657>
    MouseWheelX: typing.ClassVar[Key]  # value = <Key.MouseWheelX: 661>
    MouseWheelY: typing.ClassVar[Key]  # value = <Key.MouseWheelY: 662>
    MouseX1: typing.ClassVar[Key]  # value = <Key.MouseX1: 659>
    MouseX2: typing.ClassVar[Key]  # value = <Key.MouseX2: 660>
    N: typing.ClassVar[Key]  # value = <Key.N: 559>
    N0: typing.ClassVar[Key]  # value = <Key.N0: 536>
    N1: typing.ClassVar[Key]  # value = <Key.N1: 537>
    N2: typing.ClassVar[Key]  # value = <Key.N2: 538>
    N3: typing.ClassVar[Key]  # value = <Key.N3: 539>
    N4: typing.ClassVar[Key]  # value = <Key.N4: 540>
    N5: typing.ClassVar[Key]  # value = <Key.N5: 541>
    N6: typing.ClassVar[Key]  # value = <Key.N6: 542>
    N7: typing.ClassVar[Key]  # value = <Key.N7: 543>
    N8: typing.ClassVar[Key]  # value = <Key.N8: 544>
    N9: typing.ClassVar[Key]  # value = <Key.N9: 545>
    None: typing.ClassVar[Key]  # value = <Key.None: 0>
    NumLock: typing.ClassVar[Key]  # value = <Key.NumLock: 609>
    O: typing.ClassVar[Key]  # value = <Key.O: 560>
    P: typing.ClassVar[Key]  # value = <Key.P: 561>
    PageDown: typing.ClassVar[Key]  # value = <Key.PageDown: 518>
    PageUp: typing.ClassVar[Key]  # value = <Key.PageUp: 517>
    Pause: typing.ClassVar[Key]  # value = <Key.Pause: 611>
    Period: typing.ClassVar[Key]  # value = <Key.Period: 599>
    PrintScreen: typing.ClassVar[Key]  # value = <Key.PrintScreen: 610>
    Q: typing.ClassVar[Key]  # value = <Key.Q: 562>
    R: typing.ClassVar[Key]  # value = <Key.R: 563>
    ReservedForModAlt: typing.ClassVar[Key]  # value = <Key.ReservedForModAlt: 665>
    ReservedForModCtrl: typing.ClassVar[Key]  # value = <Key.ReservedForModCtrl: 663>
    ReservedForModShift: typing.ClassVar[Key]  # value = <Key.ReservedForModShift: 664>
    ReservedForModSuper: typing.ClassVar[Key]  # value = <Key.ReservedForModSuper: 666>
    RightAlt: typing.ClassVar[Key]  # value = <Key.RightAlt: 533>
    RightArrow: typing.ClassVar[Key]  # value = <Key.RightArrow: 514>
    RightBracket: typing.ClassVar[Key]  # value = <Key.RightBracket: 605>
    RightCtrl: typing.ClassVar[Key]  # value = <Key.RightCtrl: 531>
    RightShift: typing.ClassVar[Key]  # value = <Key.RightShift: 532>
    RightSuper: typing.ClassVar[Key]  # value = <Key.RightSuper: 534>
    S: typing.ClassVar[Key]  # value = <Key.S: 564>
    ScrollLock: typing.ClassVar[Key]  # value = <Key.ScrollLock: 608>
    Semicolon: typing.ClassVar[Key]  # value = <Key.Semicolon: 601>
    Shift: typing.ClassVar[Key]  # value = <Key.Shift: 8192>
    Slash: typing.ClassVar[Key]  # value = <Key.Slash: 600>
    Space: typing.ClassVar[Key]  # value = <Key.Space: 524>
    Super: typing.ClassVar[Key]  # value = <Key.Super: 32768>
    T: typing.ClassVar[Key]  # value = <Key.T: 565>
    Tab: typing.ClassVar[Key]  # value = <Key.Tab: 512>
    U: typing.ClassVar[Key]  # value = <Key.U: 566>
    UpArrow: typing.ClassVar[Key]  # value = <Key.UpArrow: 515>
    V: typing.ClassVar[Key]  # value = <Key.V: 567>
    W: typing.ClassVar[Key]  # value = <Key.W: 568>
    X: typing.ClassVar[Key]  # value = <Key.X: 569>
    Y: typing.ClassVar[Key]  # value = <Key.Y: 570>
    Z: typing.ClassVar[Key]  # value = <Key.Z: 571>
    __members__: typing.ClassVar[dict[str, Key]]  # value = {'None': <Key.None: 0>, 'Tab': <Key.Tab: 512>, 'LeftArrow': <Key.LeftArrow: 513>, 'RightArrow': <Key.RightArrow: 514>, 'UpArrow': <Key.UpArrow: 515>, 'DownArrow': <Key.DownArrow: 516>, 'PageUp': <Key.PageUp: 517>, 'PageDown': <Key.PageDown: 518>, 'Home': <Key.Home: 519>, 'End': <Key.End: 520>, 'Insert': <Key.Insert: 521>, 'Delete': <Key.Delete: 522>, 'Backspace': <Key.Backspace: 523>, 'Space': <Key.Space: 524>, 'Enter': <Key.Enter: 525>, 'Escape': <Key.Escape: 526>, 'LeftCtrl': <Key.LeftCtrl: 527>, 'LeftShift': <Key.LeftShift: 528>, 'LeftAlt': <Key.LeftAlt: 529>, 'LeftSuper': <Key.LeftSuper: 530>, 'RightCtrl': <Key.RightCtrl: 531>, 'RightShift': <Key.RightShift: 532>, 'RightAlt': <Key.RightAlt: 533>, 'RightSuper': <Key.RightSuper: 534>, 'Menu': <Key.Menu: 535>, 'N0': <Key.N0: 536>, 'N1': <Key.N1: 537>, 'N2': <Key.N2: 538>, 'N3': <Key.N3: 539>, 'N4': <Key.N4: 540>, 'N5': <Key.N5: 541>, 'N6': <Key.N6: 542>, 'N7': <Key.N7: 543>, 'N8': <Key.N8: 544>, 'N9': <Key.N9: 545>, 'A': <Key.A: 546>, 'B': <Key.B: 547>, 'C': <Key.C: 548>, 'D': <Key.D: 549>, 'E': <Key.E: 550>, 'F': <Key.F: 551>, 'G': <Key.G: 552>, 'H': <Key.H: 553>, 'I': <Key.I: 554>, 'J': <Key.J: 555>, 'K': <Key.K: 556>, 'L': <Key.L: 557>, 'M': <Key.M: 558>, 'N': <Key.N: 559>, 'O': <Key.O: 560>, 'P': <Key.P: 561>, 'Q': <Key.Q: 562>, 'R': <Key.R: 563>, 'S': <Key.S: 564>, 'T': <Key.T: 565>, 'U': <Key.U: 566>, 'V': <Key.V: 567>, 'W': <Key.W: 568>, 'X': <Key.X: 569>, 'Y': <Key.Y: 570>, 'Z': <Key.Z: 571>, 'F1': <Key.F1: 572>, 'F2': <Key.F2: 573>, 'F3': <Key.F3: 574>, 'F4': <Key.F4: 575>, 'F5': <Key.F5: 576>, 'F6': <Key.F6: 577>, 'F7': <Key.F7: 578>, 'F8': <Key.F8: 579>, 'F9': <Key.F9: 580>, 'F10': <Key.F10: 581>, 'F11': <Key.F11: 582>, 'F12': <Key.F12: 583>, 'F13': <Key.F13: 584>, 'F14': <Key.F14: 585>, 'F15': <Key.F15: 586>, 'F16': <Key.F16: 587>, 'F17': <Key.F17: 588>, 'F18': <Key.F18: 589>, 'F19': <Key.F19: 590>, 'F20': <Key.F20: 591>, 'F21': <Key.F21: 592>, 'F22': <Key.F22: 593>, 'F23': <Key.F23: 594>, 'F24': <Key.F24: 595>, 'Apostrophe': <Key.Apostrophe: 596>, 'Comma': <Key.Comma: 597>, 'Minus': <Key.Minus: 598>, 'Period': <Key.Period: 599>, 'Slash': <Key.Slash: 600>, 'Semicolon': <Key.Semicolon: 601>, 'Equal': <Key.Equal: 602>, 'LeftBracket': <Key.LeftBracket: 603>, 'Backslash': <Key.Backslash: 604>, 'RightBracket': <Key.RightBracket: 605>, 'GraveAccent': <Key.GraveAccent: 606>, 'CapsLock': <Key.CapsLock: 607>, 'ScrollLock': <Key.ScrollLock: 608>, 'NumLock': <Key.NumLock: 609>, 'PrintScreen': <Key.PrintScreen: 610>, 'Pause': <Key.Pause: 611>, 'Keypad0': <Key.Keypad0: 612>, 'Keypad1': <Key.Keypad1: 613>, 'Keypad2': <Key.Keypad2: 614>, 'Keypad3': <Key.Keypad3: 615>, 'Keypad4': <Key.Keypad4: 616>, 'Keypad5': <Key.Keypad5: 617>, 'Keypad6': <Key.Keypad6: 618>, 'Keypad7': <Key.Keypad7: 619>, 'Keypad8': <Key.Keypad8: 620>, 'Keypad9': <Key.Keypad9: 621>, 'KeypadDecimal': <Key.KeypadDecimal: 622>, 'KeypadDivide': <Key.KeypadDivide: 623>, 'KeypadMultiply': <Key.KeypadMultiply: 624>, 'KeypadSubtract': <Key.KeypadSubtract: 625>, 'KeypadAdd': <Key.KeypadAdd: 626>, 'KeypadEnter': <Key.KeypadEnter: 627>, 'KeypadEqual': <Key.KeypadEqual: 628>, 'AppBack': <Key.AppBack: 629>, 'AppForward': <Key.AppForward: 630>, 'GamepadStart': <Key.GamepadStart: 632>, 'GamepadBack': <Key.GamepadBack: 633>, 'GamepadFaceLeft': <Key.GamepadFaceLeft: 634>, 'GamepadFaceRight': <Key.GamepadFaceRight: 635>, 'GamepadFaceUp': <Key.GamepadFaceUp: 636>, 'GamepadFaceDown': <Key.GamepadFaceDown: 637>, 'GamepadDpadLeft': <Key.GamepadDpadLeft: 638>, 'GamepadDpadRight': <Key.GamepadDpadRight: 639>, 'GamepadDpadUp': <Key.GamepadDpadUp: 640>, 'GamepadDpadDown': <Key.GamepadDpadDown: 641>, 'GamepadL1': <Key.GamepadL1: 642>, 'GamepadR1': <Key.GamepadR1: 643>, 'GamepadL2': <Key.GamepadL2: 644>, 'GamepadR2': <Key.GamepadR2: 645>, 'GamepadL3': <Key.GamepadL3: 646>, 'GamepadR3': <Key.GamepadR3: 647>, 'GamepadLStickLeft': <Key.GamepadLStickLeft: 648>, 'GamepadLStickRight': <Key.GamepadLStickRight: 649>, 'GamepadLStickUp': <Key.GamepadLStickUp: 650>, 'GamepadLStickDown': <Key.GamepadLStickDown: 651>, 'GamepadRStickLeft': <Key.GamepadRStickLeft: 652>, 'GamepadRStickRight': <Key.GamepadRStickRight: 653>, 'GamepadRStickUp': <Key.GamepadRStickUp: 654>, 'GamepadRStickDown': <Key.GamepadRStickDown: 655>, 'MouseLeft': <Key.MouseLeft: 656>, 'MouseRight': <Key.MouseRight: 657>, 'MouseMiddle': <Key.MouseMiddle: 658>, 'MouseX1': <Key.MouseX1: 659>, 'MouseX2': <Key.MouseX2: 660>, 'MouseWheelX': <Key.MouseWheelX: 661>, 'MouseWheelY': <Key.MouseWheelY: 662>, 'ReservedForModCtrl': <Key.ReservedForModCtrl: 663>, 'ReservedForModShift': <Key.ReservedForModShift: 664>, 'ReservedForModAlt': <Key.ReservedForModAlt: 665>, 'ReservedForModSuper': <Key.ReservedForModSuper: 666>, 'Ctrl': <Key.Ctrl: 4096>, 'Shift': <Key.Shift: 8192>, 'Alt': <Key.Alt: 16384>, 'Super': <Key.Super: 32768>, 'Mask': <Key.Mask: 61440>}
    @typing.overload
    def __eq__(self, other: Key) -> bool:
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
    def __ne__(self, other: Key) -> bool:
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
class ListClipper:
    def Begin(self, items_count: typing.SupportsInt | typing.SupportsIndex, items_height: typing.SupportsFloat | typing.SupportsIndex = -1.0) -> None:
        ...
    def End(self) -> None:
        ...
    def IncludeItemByIndex(self, item_index: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def IncludeItemsByIndex(self, item_begin: typing.SupportsInt | typing.SupportsIndex, item_end: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def SeekCursorForItem(self, item_index: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def Step(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
    @property
    def DisplayEnd(self) -> int:
        ...
    @property
    def DisplayStart(self) -> int:
        ...
class MouseButton:
    """
    Members:
    
      Left
    
      Right
    
      Middle
    """
    Left: typing.ClassVar[MouseButton]  # value = <MouseButton.Left: 0>
    Middle: typing.ClassVar[MouseButton]  # value = <MouseButton.Middle: 2>
    Right: typing.ClassVar[MouseButton]  # value = <MouseButton.Right: 1>
    __members__: typing.ClassVar[dict[str, MouseButton]]  # value = {'Left': <MouseButton.Left: 0>, 'Right': <MouseButton.Right: 1>, 'Middle': <MouseButton.Middle: 2>}
    @typing.overload
    def __eq__(self, other: MouseButton) -> bool:
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
    def __ne__(self, other: MouseButton) -> bool:
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
class MouseCursor:
    """
    Members:
    
      None
    
      Arrow
    
      TextInput
    
      ResizeAll
    
      ResizeNS
    
      ResizeEW
    
      ResizeNESW
    
      ResizeNWSE
    
      Hand
    
      NotAllowed
    """
    Arrow: typing.ClassVar[MouseCursor]  # value = <MouseCursor.Arrow: 0>
    Hand: typing.ClassVar[MouseCursor]  # value = <MouseCursor.Hand: 7>
    None: typing.ClassVar[MouseCursor]  # value = <MouseCursor.None: -1>
    NotAllowed: typing.ClassVar[MouseCursor]  # value = <MouseCursor.NotAllowed: 10>
    ResizeAll: typing.ClassVar[MouseCursor]  # value = <MouseCursor.ResizeAll: 2>
    ResizeEW: typing.ClassVar[MouseCursor]  # value = <MouseCursor.ResizeEW: 4>
    ResizeNESW: typing.ClassVar[MouseCursor]  # value = <MouseCursor.ResizeNESW: 5>
    ResizeNS: typing.ClassVar[MouseCursor]  # value = <MouseCursor.ResizeNS: 3>
    ResizeNWSE: typing.ClassVar[MouseCursor]  # value = <MouseCursor.ResizeNWSE: 6>
    TextInput: typing.ClassVar[MouseCursor]  # value = <MouseCursor.TextInput: 1>
    __members__: typing.ClassVar[dict[str, MouseCursor]]  # value = {'None': <MouseCursor.None: -1>, 'Arrow': <MouseCursor.Arrow: 0>, 'TextInput': <MouseCursor.TextInput: 1>, 'ResizeAll': <MouseCursor.ResizeAll: 2>, 'ResizeNS': <MouseCursor.ResizeNS: 3>, 'ResizeEW': <MouseCursor.ResizeEW: 4>, 'ResizeNESW': <MouseCursor.ResizeNESW: 5>, 'ResizeNWSE': <MouseCursor.ResizeNWSE: 6>, 'Hand': <MouseCursor.Hand: 7>, 'NotAllowed': <MouseCursor.NotAllowed: 10>}
    @typing.overload
    def __eq__(self, other: MouseCursor) -> bool:
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
    def __ne__(self, other: MouseCursor) -> bool:
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
class MouseSource:
    """
    Members:
    
      Mouse
    
      TouchScreen
    
      Pen
    """
    Mouse: typing.ClassVar[MouseSource]  # value = <MouseSource.Mouse: 0>
    Pen: typing.ClassVar[MouseSource]  # value = <MouseSource.Pen: 2>
    TouchScreen: typing.ClassVar[MouseSource]  # value = <MouseSource.TouchScreen: 1>
    __members__: typing.ClassVar[dict[str, MouseSource]]  # value = {'Mouse': <MouseSource.Mouse: 0>, 'TouchScreen': <MouseSource.TouchScreen: 1>, 'Pen': <MouseSource.Pen: 2>}
    @typing.overload
    def __eq__(self, other: MouseSource) -> bool:
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
    def __ne__(self, other: MouseSource) -> bool:
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
class PopupFlags:
    """
    Members:
    
      None
    
      MouseButtonLeft
    
      MouseButtonRight
    
      MouseButtonMiddle
    
      MouseButtonMask
    
      NoReopen
    
      NoOpenOverExistingPopup
    
      NoOpenOverItems
    
      AnyPopupId
    
      AnyPopupLevel
    
      AnyPopup
    """
    AnyPopup: typing.ClassVar[PopupFlags]  # value = <PopupFlags.AnyPopup: 3072>
    AnyPopupId: typing.ClassVar[PopupFlags]  # value = <PopupFlags.AnyPopupId: 1024>
    AnyPopupLevel: typing.ClassVar[PopupFlags]  # value = <PopupFlags.AnyPopupLevel: 2048>
    MouseButtonLeft: typing.ClassVar[PopupFlags]  # value = <PopupFlags.MouseButtonLeft: 4>
    MouseButtonMask: typing.ClassVar[PopupFlags]  # value = <PopupFlags.MouseButtonMiddle: 12>
    MouseButtonMiddle: typing.ClassVar[PopupFlags]  # value = <PopupFlags.MouseButtonMiddle: 12>
    MouseButtonRight: typing.ClassVar[PopupFlags]  # value = <PopupFlags.MouseButtonRight: 8>
    NoOpenOverExistingPopup: typing.ClassVar[PopupFlags]  # value = <PopupFlags.NoOpenOverExistingPopup: 128>
    NoOpenOverItems: typing.ClassVar[PopupFlags]  # value = <PopupFlags.NoOpenOverItems: 256>
    NoReopen: typing.ClassVar[PopupFlags]  # value = <PopupFlags.NoReopen: 32>
    None: typing.ClassVar[PopupFlags]  # value = <PopupFlags.None: 0>
    __members__: typing.ClassVar[dict[str, PopupFlags]]  # value = {'None': <PopupFlags.None: 0>, 'MouseButtonLeft': <PopupFlags.MouseButtonLeft: 4>, 'MouseButtonRight': <PopupFlags.MouseButtonRight: 8>, 'MouseButtonMiddle': <PopupFlags.MouseButtonMiddle: 12>, 'MouseButtonMask': <PopupFlags.MouseButtonMiddle: 12>, 'NoReopen': <PopupFlags.NoReopen: 32>, 'NoOpenOverExistingPopup': <PopupFlags.NoOpenOverExistingPopup: 128>, 'NoOpenOverItems': <PopupFlags.NoOpenOverItems: 256>, 'AnyPopupId': <PopupFlags.AnyPopupId: 1024>, 'AnyPopupLevel': <PopupFlags.AnyPopupLevel: 2048>, 'AnyPopup': <PopupFlags.AnyPopup: 3072>}
    @typing.overload
    def __eq__(self, other: PopupFlags) -> bool:
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
    def __ne__(self, other: PopupFlags) -> bool:
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
class SelectableFlags:
    """
    Members:
    
      None
    
      DontClosePopups
    
      SpanAllColumns
    
      AllowDoubleClick
    
      Disabled
    
      AllowOverlap
    """
    AllowDoubleClick: typing.ClassVar[SelectableFlags]  # value = <SelectableFlags.AllowDoubleClick: 4>
    AllowOverlap: typing.ClassVar[SelectableFlags]  # value = <SelectableFlags.AllowOverlap: 16>
    Disabled: typing.ClassVar[SelectableFlags]  # value = <SelectableFlags.Disabled: 8>
    DontClosePopups: typing.ClassVar[SelectableFlags]  # value = <SelectableFlags.DontClosePopups: 1>
    None: typing.ClassVar[SelectableFlags]  # value = <SelectableFlags.None: 0>
    SpanAllColumns: typing.ClassVar[SelectableFlags]  # value = <SelectableFlags.SpanAllColumns: 2>
    __members__: typing.ClassVar[dict[str, SelectableFlags]]  # value = {'None': <SelectableFlags.None: 0>, 'DontClosePopups': <SelectableFlags.DontClosePopups: 1>, 'SpanAllColumns': <SelectableFlags.SpanAllColumns: 2>, 'AllowDoubleClick': <SelectableFlags.AllowDoubleClick: 4>, 'Disabled': <SelectableFlags.Disabled: 8>, 'AllowOverlap': <SelectableFlags.AllowOverlap: 16>}
    @typing.overload
    def __eq__(self, other: SelectableFlags) -> bool:
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
    def __ne__(self, other: SelectableFlags) -> bool:
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
class SliderFlags:
    """
    Members:
    
      None
    
      AlwaysClamp
    
      Logarithmic
    
      NoRoundToFormat
    
      NoInput
    
      WrapAround
    
      InvalidMask
    """
    AlwaysClamp: typing.ClassVar[SliderFlags]  # value = <SliderFlags.AlwaysClamp: 1536>
    InvalidMask: typing.ClassVar[SliderFlags]  # value = <SliderFlags.InvalidMask: 1879048207>
    Logarithmic: typing.ClassVar[SliderFlags]  # value = <SliderFlags.Logarithmic: 32>
    NoInput: typing.ClassVar[SliderFlags]  # value = <SliderFlags.NoInput: 128>
    NoRoundToFormat: typing.ClassVar[SliderFlags]  # value = <SliderFlags.NoRoundToFormat: 64>
    None: typing.ClassVar[SliderFlags]  # value = <SliderFlags.None: 0>
    WrapAround: typing.ClassVar[SliderFlags]  # value = <SliderFlags.WrapAround: 256>
    __members__: typing.ClassVar[dict[str, SliderFlags]]  # value = {'None': <SliderFlags.None: 0>, 'AlwaysClamp': <SliderFlags.AlwaysClamp: 1536>, 'Logarithmic': <SliderFlags.Logarithmic: 32>, 'NoRoundToFormat': <SliderFlags.NoRoundToFormat: 64>, 'NoInput': <SliderFlags.NoInput: 128>, 'WrapAround': <SliderFlags.WrapAround: 256>, 'InvalidMask': <SliderFlags.InvalidMask: 1879048207>}
    @typing.overload
    def __eq__(self, other: SliderFlags) -> bool:
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
    def __ne__(self, other: SliderFlags) -> bool:
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
class SortDirection:
    """
    Members:
    
      None
    
      Ascending
    
      Descending
    """
    Ascending: typing.ClassVar[SortDirection]  # value = <SortDirection.Ascending: 1>
    Descending: typing.ClassVar[SortDirection]  # value = <SortDirection.Descending: 2>
    None: typing.ClassVar[SortDirection]  # value = <SortDirection.None: 0>
    __members__: typing.ClassVar[dict[str, SortDirection]]  # value = {'None': <SortDirection.None: 0>, 'Ascending': <SortDirection.Ascending: 1>, 'Descending': <SortDirection.Descending: 2>}
    @typing.overload
    def __eq__(self, other: SortDirection) -> bool:
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
    def __ne__(self, other: SortDirection) -> bool:
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
class Style:
    FramePadding: Vec2
    ItemSpacing: Vec2
    WindowPadding: Vec2
    @property
    def FontScaleMain(self) -> float:
        ...
    @FontScaleMain.setter
    def FontScaleMain(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class StyleVar:
    """
    Members:
    
      Alpha
    
      DisabledAlpha
    
      WindowPadding
    
      WindowRounding
    
      WindowBorderSize
    
      WindowMinSize
    
      WindowTitleAlign
    
      ChildRounding
    
      ChildBorderSize
    
      PopupRounding
    
      PopupBorderSize
    
      FramePadding
    
      FrameRounding
    
      FrameBorderSize
    
      ItemSpacing
    
      ItemInnerSpacing
    
      IndentSpacing
    
      CellPadding
    
      ScrollbarSize
    
      ScrollbarRounding
    
      GrabMinSize
    
      GrabRounding
    
      TabRounding
    
      TabBorderSize
    
      TabBarBorderSize
    
      TableAngledHeadersAngle
    
      TableAngledHeadersTextAlign
    
      ButtonTextAlign
    
      SelectableTextAlign
    
      SeparatorTextBorderSize
    
      SeparatorTextAlign
    
      SeparatorTextPadding
    
      DockingSeparatorSize
    """
    Alpha: typing.ClassVar[StyleVar]  # value = <StyleVar.Alpha: 0>
    ButtonTextAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.ButtonTextAlign: 38>
    CellPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.CellPadding: 17>
    ChildBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.ChildBorderSize: 8>
    ChildRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.ChildRounding: 7>
    DisabledAlpha: typing.ClassVar[StyleVar]  # value = <StyleVar.DisabledAlpha: 1>
    DockingSeparatorSize: typing.ClassVar[StyleVar]  # value = <StyleVar.DockingSeparatorSize: 44>
    FrameBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.FrameBorderSize: 13>
    FramePadding: typing.ClassVar[StyleVar]  # value = <StyleVar.FramePadding: 11>
    FrameRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.FrameRounding: 12>
    GrabMinSize: typing.ClassVar[StyleVar]  # value = <StyleVar.GrabMinSize: 21>
    GrabRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.GrabRounding: 22>
    IndentSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.IndentSpacing: 16>
    ItemInnerSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.ItemInnerSpacing: 15>
    ItemSpacing: typing.ClassVar[StyleVar]  # value = <StyleVar.ItemSpacing: 14>
    PopupBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.PopupBorderSize: 10>
    PopupRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.PopupRounding: 9>
    ScrollbarRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.ScrollbarRounding: 19>
    ScrollbarSize: typing.ClassVar[StyleVar]  # value = <StyleVar.ScrollbarSize: 18>
    SelectableTextAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.SelectableTextAlign: 39>
    SeparatorTextAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.SeparatorTextAlign: 42>
    SeparatorTextBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.SeparatorTextBorderSize: 41>
    SeparatorTextPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.SeparatorTextPadding: 43>
    TabBarBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.TabBarBorderSize: 29>
    TabBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.TabBorderSize: 26>
    TabRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.TabRounding: 25>
    TableAngledHeadersAngle: typing.ClassVar[StyleVar]  # value = <StyleVar.TableAngledHeadersAngle: 31>
    TableAngledHeadersTextAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.TableAngledHeadersTextAlign: 32>
    WindowBorderSize: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowBorderSize: 4>
    WindowMinSize: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowMinSize: 5>
    WindowPadding: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowPadding: 2>
    WindowRounding: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowRounding: 3>
    WindowTitleAlign: typing.ClassVar[StyleVar]  # value = <StyleVar.WindowTitleAlign: 6>
    __members__: typing.ClassVar[dict[str, StyleVar]]  # value = {'Alpha': <StyleVar.Alpha: 0>, 'DisabledAlpha': <StyleVar.DisabledAlpha: 1>, 'WindowPadding': <StyleVar.WindowPadding: 2>, 'WindowRounding': <StyleVar.WindowRounding: 3>, 'WindowBorderSize': <StyleVar.WindowBorderSize: 4>, 'WindowMinSize': <StyleVar.WindowMinSize: 5>, 'WindowTitleAlign': <StyleVar.WindowTitleAlign: 6>, 'ChildRounding': <StyleVar.ChildRounding: 7>, 'ChildBorderSize': <StyleVar.ChildBorderSize: 8>, 'PopupRounding': <StyleVar.PopupRounding: 9>, 'PopupBorderSize': <StyleVar.PopupBorderSize: 10>, 'FramePadding': <StyleVar.FramePadding: 11>, 'FrameRounding': <StyleVar.FrameRounding: 12>, 'FrameBorderSize': <StyleVar.FrameBorderSize: 13>, 'ItemSpacing': <StyleVar.ItemSpacing: 14>, 'ItemInnerSpacing': <StyleVar.ItemInnerSpacing: 15>, 'IndentSpacing': <StyleVar.IndentSpacing: 16>, 'CellPadding': <StyleVar.CellPadding: 17>, 'ScrollbarSize': <StyleVar.ScrollbarSize: 18>, 'ScrollbarRounding': <StyleVar.ScrollbarRounding: 19>, 'GrabMinSize': <StyleVar.GrabMinSize: 21>, 'GrabRounding': <StyleVar.GrabRounding: 22>, 'TabRounding': <StyleVar.TabRounding: 25>, 'TabBorderSize': <StyleVar.TabBorderSize: 26>, 'TabBarBorderSize': <StyleVar.TabBarBorderSize: 29>, 'TableAngledHeadersAngle': <StyleVar.TableAngledHeadersAngle: 31>, 'TableAngledHeadersTextAlign': <StyleVar.TableAngledHeadersTextAlign: 32>, 'ButtonTextAlign': <StyleVar.ButtonTextAlign: 38>, 'SelectableTextAlign': <StyleVar.SelectableTextAlign: 39>, 'SeparatorTextBorderSize': <StyleVar.SeparatorTextBorderSize: 41>, 'SeparatorTextAlign': <StyleVar.SeparatorTextAlign: 42>, 'SeparatorTextPadding': <StyleVar.SeparatorTextPadding: 43>, 'DockingSeparatorSize': <StyleVar.DockingSeparatorSize: 44>}
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
class TabBarFlags:
    """
    Members:
    
      None
    
      Reorderable
    
      AutoSelectNewTabs
    
      TabListPopupButton
    
      NoCloseWithMiddleMouseButton
    
      NoTabListScrollingButtons
    
      NoTooltip
    
      DrawSelectedOverline
    
      FittingPolicyResizeDown
    
      FittingPolicyScroll
    
      FittingPolicyMask
    
      FittingPolicyDefault
    """
    AutoSelectNewTabs: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.AutoSelectNewTabs: 2>
    DrawSelectedOverline: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.DrawSelectedOverline: 64>
    FittingPolicyDefault: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.FittingPolicyDefault: 128>
    FittingPolicyMask: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.FittingPolicyMask: 896>
    FittingPolicyResizeDown: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.FittingPolicyResizeDown: 256>
    FittingPolicyScroll: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.FittingPolicyScroll: 512>
    NoCloseWithMiddleMouseButton: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.NoCloseWithMiddleMouseButton: 8>
    NoTabListScrollingButtons: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.NoTabListScrollingButtons: 16>
    NoTooltip: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.NoTooltip: 32>
    None: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.None: 0>
    Reorderable: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.Reorderable: 1>
    TabListPopupButton: typing.ClassVar[TabBarFlags]  # value = <TabBarFlags.TabListPopupButton: 4>
    __members__: typing.ClassVar[dict[str, TabBarFlags]]  # value = {'None': <TabBarFlags.None: 0>, 'Reorderable': <TabBarFlags.Reorderable: 1>, 'AutoSelectNewTabs': <TabBarFlags.AutoSelectNewTabs: 2>, 'TabListPopupButton': <TabBarFlags.TabListPopupButton: 4>, 'NoCloseWithMiddleMouseButton': <TabBarFlags.NoCloseWithMiddleMouseButton: 8>, 'NoTabListScrollingButtons': <TabBarFlags.NoTabListScrollingButtons: 16>, 'NoTooltip': <TabBarFlags.NoTooltip: 32>, 'DrawSelectedOverline': <TabBarFlags.DrawSelectedOverline: 64>, 'FittingPolicyResizeDown': <TabBarFlags.FittingPolicyResizeDown: 256>, 'FittingPolicyScroll': <TabBarFlags.FittingPolicyScroll: 512>, 'FittingPolicyMask': <TabBarFlags.FittingPolicyMask: 896>, 'FittingPolicyDefault': <TabBarFlags.FittingPolicyDefault: 128>}
    @typing.overload
    def __eq__(self, other: TabBarFlags) -> bool:
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
    def __ne__(self, other: TabBarFlags) -> bool:
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
class TabItemFlags:
    """
    Members:
    
      None
    
      UnsavedDocument
    
      SetSelected
    
      NoCloseWithMiddleMouseButton
    
      NoPushId
    
      NoTooltip
    
      NoReorder
    
      Leading
    
      Trailing
    
      NoAssumedClosure
    """
    Leading: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.Leading: 64>
    NoAssumedClosure: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.NoAssumedClosure: 256>
    NoCloseWithMiddleMouseButton: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.NoCloseWithMiddleMouseButton: 4>
    NoPushId: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.NoPushId: 8>
    NoReorder: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.NoReorder: 32>
    NoTooltip: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.NoTooltip: 16>
    None: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.None: 0>
    SetSelected: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.SetSelected: 2>
    Trailing: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.Trailing: 128>
    UnsavedDocument: typing.ClassVar[TabItemFlags]  # value = <TabItemFlags.UnsavedDocument: 1>
    __members__: typing.ClassVar[dict[str, TabItemFlags]]  # value = {'None': <TabItemFlags.None: 0>, 'UnsavedDocument': <TabItemFlags.UnsavedDocument: 1>, 'SetSelected': <TabItemFlags.SetSelected: 2>, 'NoCloseWithMiddleMouseButton': <TabItemFlags.NoCloseWithMiddleMouseButton: 4>, 'NoPushId': <TabItemFlags.NoPushId: 8>, 'NoTooltip': <TabItemFlags.NoTooltip: 16>, 'NoReorder': <TabItemFlags.NoReorder: 32>, 'Leading': <TabItemFlags.Leading: 64>, 'Trailing': <TabItemFlags.Trailing: 128>, 'NoAssumedClosure': <TabItemFlags.NoAssumedClosure: 256>}
    @typing.overload
    def __eq__(self, other: TabItemFlags) -> bool:
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
    def __ne__(self, other: TabItemFlags) -> bool:
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
class TableBgTarget:
    """
    Members:
    
      None
    
      RowBg0
    
      RowBg1
    
      CellBg
    """
    CellBg: typing.ClassVar[TableBgTarget]  # value = <TableBgTarget.CellBg: 3>
    None: typing.ClassVar[TableBgTarget]  # value = <TableBgTarget.None: 0>
    RowBg0: typing.ClassVar[TableBgTarget]  # value = <TableBgTarget.RowBg0: 1>
    RowBg1: typing.ClassVar[TableBgTarget]  # value = <TableBgTarget.RowBg1: 2>
    __members__: typing.ClassVar[dict[str, TableBgTarget]]  # value = {'None': <TableBgTarget.None: 0>, 'RowBg0': <TableBgTarget.RowBg0: 1>, 'RowBg1': <TableBgTarget.RowBg1: 2>, 'CellBg': <TableBgTarget.CellBg: 3>}
    @typing.overload
    def __eq__(self, other: TableBgTarget) -> bool:
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
    def __ne__(self, other: TableBgTarget) -> bool:
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
class TableColumnFlags:
    """
    Members:
    
      None
    
      Disabled
    
      DefaultHide
    
      DefaultSort
    
      WidthStretch
    
      WidthFixed
    
      NoResize
    
      NoReorder
    
      NoHide
    
      NoClip
    
      NoSort
    
      NoSortAscending
    
      NoSortDescending
    
      NoHeaderLabel
    
      NoHeaderWidth
    
      PreferSortAscending
    
      PreferSortDescending
    
      IndentEnable
    
      IndentDisable
    
      AngledHeader
    
      IsEnabled
    
      IsVisible
    
      IsSorted
    
      IsHovered
    
      WidthMask
    
      IndentMask
    
      StatusMask
    
      NoDirectResize
    """
    AngledHeader: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.AngledHeader: 262144>
    DefaultHide: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.DefaultHide: 2>
    DefaultSort: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.DefaultSort: 4>
    Disabled: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.Disabled: 1>
    IndentDisable: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IndentDisable: 131072>
    IndentEnable: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IndentEnable: 65536>
    IndentMask: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IndentMask: 196608>
    IsEnabled: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IsEnabled: 16777216>
    IsHovered: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IsHovered: 134217728>
    IsSorted: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IsSorted: 67108864>
    IsVisible: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.IsVisible: 33554432>
    NoClip: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoClip: 256>
    NoDirectResize: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoDirectResize: 1073741824>
    NoHeaderLabel: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoHeaderLabel: 4096>
    NoHeaderWidth: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoHeaderWidth: 8192>
    NoHide: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoHide: 128>
    NoReorder: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoReorder: 64>
    NoResize: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoResize: 32>
    NoSort: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoSort: 512>
    NoSortAscending: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoSortAscending: 1024>
    NoSortDescending: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.NoSortDescending: 2048>
    None: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.None: 0>
    PreferSortAscending: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.PreferSortAscending: 16384>
    PreferSortDescending: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.PreferSortDescending: 32768>
    StatusMask: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.StatusMask: 251658240>
    WidthFixed: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.WidthFixed: 16>
    WidthMask: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.WidthMask: 24>
    WidthStretch: typing.ClassVar[TableColumnFlags]  # value = <TableColumnFlags.WidthStretch: 8>
    __members__: typing.ClassVar[dict[str, TableColumnFlags]]  # value = {'None': <TableColumnFlags.None: 0>, 'Disabled': <TableColumnFlags.Disabled: 1>, 'DefaultHide': <TableColumnFlags.DefaultHide: 2>, 'DefaultSort': <TableColumnFlags.DefaultSort: 4>, 'WidthStretch': <TableColumnFlags.WidthStretch: 8>, 'WidthFixed': <TableColumnFlags.WidthFixed: 16>, 'NoResize': <TableColumnFlags.NoResize: 32>, 'NoReorder': <TableColumnFlags.NoReorder: 64>, 'NoHide': <TableColumnFlags.NoHide: 128>, 'NoClip': <TableColumnFlags.NoClip: 256>, 'NoSort': <TableColumnFlags.NoSort: 512>, 'NoSortAscending': <TableColumnFlags.NoSortAscending: 1024>, 'NoSortDescending': <TableColumnFlags.NoSortDescending: 2048>, 'NoHeaderLabel': <TableColumnFlags.NoHeaderLabel: 4096>, 'NoHeaderWidth': <TableColumnFlags.NoHeaderWidth: 8192>, 'PreferSortAscending': <TableColumnFlags.PreferSortAscending: 16384>, 'PreferSortDescending': <TableColumnFlags.PreferSortDescending: 32768>, 'IndentEnable': <TableColumnFlags.IndentEnable: 65536>, 'IndentDisable': <TableColumnFlags.IndentDisable: 131072>, 'AngledHeader': <TableColumnFlags.AngledHeader: 262144>, 'IsEnabled': <TableColumnFlags.IsEnabled: 16777216>, 'IsVisible': <TableColumnFlags.IsVisible: 33554432>, 'IsSorted': <TableColumnFlags.IsSorted: 67108864>, 'IsHovered': <TableColumnFlags.IsHovered: 134217728>, 'WidthMask': <TableColumnFlags.WidthMask: 24>, 'IndentMask': <TableColumnFlags.IndentMask: 196608>, 'StatusMask': <TableColumnFlags.StatusMask: 251658240>, 'NoDirectResize': <TableColumnFlags.NoDirectResize: 1073741824>}
    @typing.overload
    def __eq__(self, other: TableColumnFlags) -> bool:
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
    def __ne__(self, other: TableColumnFlags) -> bool:
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
class TableFlags:
    """
    Members:
    
      None
    
      Resizable
    
      Reorderable
    
      Hideable
    
      Sortable
    
      NoSavedSettings
    
      ContextMenuInBody
    
      RowBg
    
      BordersInnerH
    
      BordersOuterH
    
      BordersInnerV
    
      BordersOuterV
    
      BordersH
    
      BordersV
    
      BordersInner
    
      BordersOuter
    
      Borders
    
      NoBordersInBody
    
      NoBordersInBodyUntilResize
    
      SizingFixedFit
    
      SizingFixedSame
    
      SizingStretchProp
    
      SizingStretchSame
    
      NoHostExtendX
    
      NoHostExtendY
    
      NoKeepColumnsVisible
    
      PreciseWidths
    
      NoClip
    
      PadOuterX
    
      NoPadOuterX
    
      NoPadInnerX
    
      ScrollX
    
      ScrollY
    
      SortMulti
    
      SortTristate
    
      HighlightHoveredColumn
    
      SizingMask
    """
    Borders: typing.ClassVar[TableFlags]  # value = <TableFlags.Borders: 1920>
    BordersH: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersH: 384>
    BordersInner: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersInner: 640>
    BordersInnerH: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersInnerH: 128>
    BordersInnerV: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersInnerV: 512>
    BordersOuter: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersOuter: 1280>
    BordersOuterH: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersOuterH: 256>
    BordersOuterV: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersOuterV: 1024>
    BordersV: typing.ClassVar[TableFlags]  # value = <TableFlags.BordersV: 1536>
    ContextMenuInBody: typing.ClassVar[TableFlags]  # value = <TableFlags.ContextMenuInBody: 32>
    Hideable: typing.ClassVar[TableFlags]  # value = <TableFlags.Hideable: 4>
    HighlightHoveredColumn: typing.ClassVar[TableFlags]  # value = <TableFlags.HighlightHoveredColumn: 268435456>
    NoBordersInBody: typing.ClassVar[TableFlags]  # value = <TableFlags.NoBordersInBody: 2048>
    NoBordersInBodyUntilResize: typing.ClassVar[TableFlags]  # value = <TableFlags.NoBordersInBodyUntilResize: 4096>
    NoClip: typing.ClassVar[TableFlags]  # value = <TableFlags.NoClip: 1048576>
    NoHostExtendX: typing.ClassVar[TableFlags]  # value = <TableFlags.NoHostExtendX: 65536>
    NoHostExtendY: typing.ClassVar[TableFlags]  # value = <TableFlags.NoHostExtendY: 131072>
    NoKeepColumnsVisible: typing.ClassVar[TableFlags]  # value = <TableFlags.NoKeepColumnsVisible: 262144>
    NoPadInnerX: typing.ClassVar[TableFlags]  # value = <TableFlags.NoPadInnerX: 8388608>
    NoPadOuterX: typing.ClassVar[TableFlags]  # value = <TableFlags.NoPadOuterX: 4194304>
    NoSavedSettings: typing.ClassVar[TableFlags]  # value = <TableFlags.NoSavedSettings: 16>
    None: typing.ClassVar[TableFlags]  # value = <TableFlags.None: 0>
    PadOuterX: typing.ClassVar[TableFlags]  # value = <TableFlags.PadOuterX: 2097152>
    PreciseWidths: typing.ClassVar[TableFlags]  # value = <TableFlags.PreciseWidths: 524288>
    Reorderable: typing.ClassVar[TableFlags]  # value = <TableFlags.Reorderable: 2>
    Resizable: typing.ClassVar[TableFlags]  # value = <TableFlags.Resizable: 1>
    RowBg: typing.ClassVar[TableFlags]  # value = <TableFlags.RowBg: 64>
    ScrollX: typing.ClassVar[TableFlags]  # value = <TableFlags.ScrollX: 16777216>
    ScrollY: typing.ClassVar[TableFlags]  # value = <TableFlags.ScrollY: 33554432>
    SizingFixedFit: typing.ClassVar[TableFlags]  # value = <TableFlags.SizingFixedFit: 8192>
    SizingFixedSame: typing.ClassVar[TableFlags]  # value = <TableFlags.SizingFixedSame: 16384>
    SizingMask: typing.ClassVar[TableFlags]  # value = <TableFlags.SizingMask: 57344>
    SizingStretchProp: typing.ClassVar[TableFlags]  # value = <TableFlags.SizingStretchProp: 24576>
    SizingStretchSame: typing.ClassVar[TableFlags]  # value = <TableFlags.SizingStretchSame: 32768>
    SortMulti: typing.ClassVar[TableFlags]  # value = <TableFlags.SortMulti: 67108864>
    SortTristate: typing.ClassVar[TableFlags]  # value = <TableFlags.SortTristate: 134217728>
    Sortable: typing.ClassVar[TableFlags]  # value = <TableFlags.Sortable: 8>
    __members__: typing.ClassVar[dict[str, TableFlags]]  # value = {'None': <TableFlags.None: 0>, 'Resizable': <TableFlags.Resizable: 1>, 'Reorderable': <TableFlags.Reorderable: 2>, 'Hideable': <TableFlags.Hideable: 4>, 'Sortable': <TableFlags.Sortable: 8>, 'NoSavedSettings': <TableFlags.NoSavedSettings: 16>, 'ContextMenuInBody': <TableFlags.ContextMenuInBody: 32>, 'RowBg': <TableFlags.RowBg: 64>, 'BordersInnerH': <TableFlags.BordersInnerH: 128>, 'BordersOuterH': <TableFlags.BordersOuterH: 256>, 'BordersInnerV': <TableFlags.BordersInnerV: 512>, 'BordersOuterV': <TableFlags.BordersOuterV: 1024>, 'BordersH': <TableFlags.BordersH: 384>, 'BordersV': <TableFlags.BordersV: 1536>, 'BordersInner': <TableFlags.BordersInner: 640>, 'BordersOuter': <TableFlags.BordersOuter: 1280>, 'Borders': <TableFlags.Borders: 1920>, 'NoBordersInBody': <TableFlags.NoBordersInBody: 2048>, 'NoBordersInBodyUntilResize': <TableFlags.NoBordersInBodyUntilResize: 4096>, 'SizingFixedFit': <TableFlags.SizingFixedFit: 8192>, 'SizingFixedSame': <TableFlags.SizingFixedSame: 16384>, 'SizingStretchProp': <TableFlags.SizingStretchProp: 24576>, 'SizingStretchSame': <TableFlags.SizingStretchSame: 32768>, 'NoHostExtendX': <TableFlags.NoHostExtendX: 65536>, 'NoHostExtendY': <TableFlags.NoHostExtendY: 131072>, 'NoKeepColumnsVisible': <TableFlags.NoKeepColumnsVisible: 262144>, 'PreciseWidths': <TableFlags.PreciseWidths: 524288>, 'NoClip': <TableFlags.NoClip: 1048576>, 'PadOuterX': <TableFlags.PadOuterX: 2097152>, 'NoPadOuterX': <TableFlags.NoPadOuterX: 4194304>, 'NoPadInnerX': <TableFlags.NoPadInnerX: 8388608>, 'ScrollX': <TableFlags.ScrollX: 16777216>, 'ScrollY': <TableFlags.ScrollY: 33554432>, 'SortMulti': <TableFlags.SortMulti: 67108864>, 'SortTristate': <TableFlags.SortTristate: 134217728>, 'HighlightHoveredColumn': <TableFlags.HighlightHoveredColumn: 268435456>, 'SizingMask': <TableFlags.SizingMask: 57344>}
    @typing.overload
    def __eq__(self, other: TableFlags) -> bool:
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
    def __ne__(self, other: TableFlags) -> bool:
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
class TableRowFlags:
    """
    Members:
    
      None
    
      Headers
    """
    Headers: typing.ClassVar[TableRowFlags]  # value = <TableRowFlags.Headers: 1>
    None: typing.ClassVar[TableRowFlags]  # value = <TableRowFlags.None: 0>
    __members__: typing.ClassVar[dict[str, TableRowFlags]]  # value = {'None': <TableRowFlags.None: 0>, 'Headers': <TableRowFlags.Headers: 1>}
    @typing.overload
    def __eq__(self, other: TableRowFlags) -> bool:
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
    def __ne__(self, other: TableRowFlags) -> bool:
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
class TreeNodeFlags:
    """
    Members:
    
      None
    
      Selected
    
      Framed
    
      AllowOverlap
    
      NoTreePushOnOpen
    
      NoAutoOpenOnLog
    
      DefaultOpen
    
      OpenOnDoubleClick
    
      OpenOnArrow
    
      Leaf
    
      Bullet
    
      FramePadding
    
      SpanAvailWidth
    
      SpanFullWidth
    
      SpanLabelWidth
    
      SpanAllColumns
    
      NavLeftJumpsBackHere
    
      CollapsingHeader
    """
    AllowOverlap: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.AllowOverlap: 4>
    Bullet: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.Bullet: 512>
    CollapsingHeader: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.CollapsingHeader: 26>
    DefaultOpen: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.DefaultOpen: 32>
    FramePadding: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.FramePadding: 1024>
    Framed: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.Framed: 2>
    Leaf: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.Leaf: 256>
    NavLeftJumpsBackHere: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.NavLeftJumpsBackHere: 131072>
    NoAutoOpenOnLog: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.NoAutoOpenOnLog: 16>
    NoTreePushOnOpen: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.NoTreePushOnOpen: 8>
    None: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.None: 0>
    OpenOnArrow: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.OpenOnArrow: 128>
    OpenOnDoubleClick: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.OpenOnDoubleClick: 64>
    Selected: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.Selected: 1>
    SpanAllColumns: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.SpanAllColumns: 16384>
    SpanAvailWidth: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.SpanAvailWidth: 2048>
    SpanFullWidth: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.SpanFullWidth: 4096>
    SpanLabelWidth: typing.ClassVar[TreeNodeFlags]  # value = <TreeNodeFlags.SpanLabelWidth: 8192>
    __members__: typing.ClassVar[dict[str, TreeNodeFlags]]  # value = {'None': <TreeNodeFlags.None: 0>, 'Selected': <TreeNodeFlags.Selected: 1>, 'Framed': <TreeNodeFlags.Framed: 2>, 'AllowOverlap': <TreeNodeFlags.AllowOverlap: 4>, 'NoTreePushOnOpen': <TreeNodeFlags.NoTreePushOnOpen: 8>, 'NoAutoOpenOnLog': <TreeNodeFlags.NoAutoOpenOnLog: 16>, 'DefaultOpen': <TreeNodeFlags.DefaultOpen: 32>, 'OpenOnDoubleClick': <TreeNodeFlags.OpenOnDoubleClick: 64>, 'OpenOnArrow': <TreeNodeFlags.OpenOnArrow: 128>, 'Leaf': <TreeNodeFlags.Leaf: 256>, 'Bullet': <TreeNodeFlags.Bullet: 512>, 'FramePadding': <TreeNodeFlags.FramePadding: 1024>, 'SpanAvailWidth': <TreeNodeFlags.SpanAvailWidth: 2048>, 'SpanFullWidth': <TreeNodeFlags.SpanFullWidth: 4096>, 'SpanLabelWidth': <TreeNodeFlags.SpanLabelWidth: 8192>, 'SpanAllColumns': <TreeNodeFlags.SpanAllColumns: 16384>, 'NavLeftJumpsBackHere': <TreeNodeFlags.NavLeftJumpsBackHere: 131072>, 'CollapsingHeader': <TreeNodeFlags.CollapsingHeader: 26>}
    @typing.overload
    def __eq__(self, other: TreeNodeFlags) -> bool:
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
    def __ne__(self, other: TreeNodeFlags) -> bool:
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
class Vec2:
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
class Vec4:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, _x: typing.SupportsFloat | typing.SupportsIndex, _y: typing.SupportsFloat | typing.SupportsIndex, _z: typing.SupportsFloat | typing.SupportsIndex, _w: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def w(self) -> float:
        ...
    @w.setter
    def w(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
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
    @property
    def z(self) -> float:
        ...
    @z.setter
    def z(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class WindowFlags:
    """
    Members:
    
      None
    
      NoTitleBar
    
      NoResize
    
      NoMove
    
      NoScrollbar
    
      NoScrollWithMouse
    
      NoCollapse
    
      AlwaysAutoResize
    
      NoBackground
    
      NoSavedSettings
    
      NoMouseInputs
    
      MenuBar
    
      HorizontalScrollbar
    
      NoFocusOnAppearing
    
      NoBringToFrontOnFocus
    
      AlwaysVerticalScrollbar
    
      AlwaysHorizontalScrollbar
    
      NoNavInputs
    
      NoNavFocus
    
      UnsavedDocument
    
      NoDocking
    
      NoNav
    
      NoDecoration
    
      NoInputs
    
      ChildWindow
    
      Tooltip
    
      Popup
    
      Modal
    
      ChildMenu
    
      DockNodeHost
    """
    AlwaysAutoResize: typing.ClassVar[WindowFlags]  # value = <WindowFlags.AlwaysAutoResize: 64>
    AlwaysHorizontalScrollbar: typing.ClassVar[WindowFlags]  # value = <WindowFlags.AlwaysHorizontalScrollbar: 32768>
    AlwaysVerticalScrollbar: typing.ClassVar[WindowFlags]  # value = <WindowFlags.AlwaysVerticalScrollbar: 16384>
    ChildMenu: typing.ClassVar[WindowFlags]  # value = <WindowFlags.ChildMenu: 268435456>
    ChildWindow: typing.ClassVar[WindowFlags]  # value = <WindowFlags.ChildWindow: 16777216>
    DockNodeHost: typing.ClassVar[WindowFlags]  # value = <WindowFlags.DockNodeHost: 8388608>
    HorizontalScrollbar: typing.ClassVar[WindowFlags]  # value = <WindowFlags.HorizontalScrollbar: 2048>
    MenuBar: typing.ClassVar[WindowFlags]  # value = <WindowFlags.MenuBar: 1024>
    Modal: typing.ClassVar[WindowFlags]  # value = <WindowFlags.Modal: 134217728>
    NoBackground: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoBackground: 128>
    NoBringToFrontOnFocus: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoBringToFrontOnFocus: 8192>
    NoCollapse: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoCollapse: 32>
    NoDecoration: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoDecoration: 43>
    NoDocking: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoDocking: 524288>
    NoFocusOnAppearing: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoFocusOnAppearing: 4096>
    NoInputs: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoInputs: 197120>
    NoMouseInputs: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoMouseInputs: 512>
    NoMove: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoMove: 4>
    NoNav: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoNav: 196608>
    NoNavFocus: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoNavFocus: 131072>
    NoNavInputs: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoNavInputs: 65536>
    NoResize: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoResize: 2>
    NoSavedSettings: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoSavedSettings: 256>
    NoScrollWithMouse: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoScrollWithMouse: 16>
    NoScrollbar: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoScrollbar: 8>
    NoTitleBar: typing.ClassVar[WindowFlags]  # value = <WindowFlags.NoTitleBar: 1>
    None: typing.ClassVar[WindowFlags]  # value = <WindowFlags.None: 0>
    Popup: typing.ClassVar[WindowFlags]  # value = <WindowFlags.Popup: 67108864>
    Tooltip: typing.ClassVar[WindowFlags]  # value = <WindowFlags.Tooltip: 33554432>
    UnsavedDocument: typing.ClassVar[WindowFlags]  # value = <WindowFlags.UnsavedDocument: 262144>
    __members__: typing.ClassVar[dict[str, WindowFlags]]  # value = {'None': <WindowFlags.None: 0>, 'NoTitleBar': <WindowFlags.NoTitleBar: 1>, 'NoResize': <WindowFlags.NoResize: 2>, 'NoMove': <WindowFlags.NoMove: 4>, 'NoScrollbar': <WindowFlags.NoScrollbar: 8>, 'NoScrollWithMouse': <WindowFlags.NoScrollWithMouse: 16>, 'NoCollapse': <WindowFlags.NoCollapse: 32>, 'AlwaysAutoResize': <WindowFlags.AlwaysAutoResize: 64>, 'NoBackground': <WindowFlags.NoBackground: 128>, 'NoSavedSettings': <WindowFlags.NoSavedSettings: 256>, 'NoMouseInputs': <WindowFlags.NoMouseInputs: 512>, 'MenuBar': <WindowFlags.MenuBar: 1024>, 'HorizontalScrollbar': <WindowFlags.HorizontalScrollbar: 2048>, 'NoFocusOnAppearing': <WindowFlags.NoFocusOnAppearing: 4096>, 'NoBringToFrontOnFocus': <WindowFlags.NoBringToFrontOnFocus: 8192>, 'AlwaysVerticalScrollbar': <WindowFlags.AlwaysVerticalScrollbar: 16384>, 'AlwaysHorizontalScrollbar': <WindowFlags.AlwaysHorizontalScrollbar: 32768>, 'NoNavInputs': <WindowFlags.NoNavInputs: 65536>, 'NoNavFocus': <WindowFlags.NoNavFocus: 131072>, 'UnsavedDocument': <WindowFlags.UnsavedDocument: 262144>, 'NoDocking': <WindowFlags.NoDocking: 524288>, 'NoNav': <WindowFlags.NoNav: 196608>, 'NoDecoration': <WindowFlags.NoDecoration: 43>, 'NoInputs': <WindowFlags.NoInputs: 197120>, 'ChildWindow': <WindowFlags.ChildWindow: 16777216>, 'Tooltip': <WindowFlags.Tooltip: 33554432>, 'Popup': <WindowFlags.Popup: 67108864>, 'Modal': <WindowFlags.Modal: 134217728>, 'ChildMenu': <WindowFlags.ChildMenu: 268435456>, 'DockNodeHost': <WindowFlags.DockNodeHost: 8388608>}
    @typing.overload
    def __eq__(self, other: WindowFlags) -> bool:
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
    def __ne__(self, other: WindowFlags) -> bool:
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
def AlignTextToFramePadding() -> None:
    ...
def ArrowButton(str_id: str, dir: Dir) -> bool:
    ...
def Begin(name: str, p_open: bool = None, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, bool]:
    ...
def BeginChild(str_id: str, size: Vec2 = ..., child_flags: typing.SupportsInt | typing.SupportsIndex = 0, window_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginChildId(id: typing.SupportsInt | typing.SupportsIndex, size: Vec2 = ..., child_flags: typing.SupportsInt | typing.SupportsIndex = 0, window_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginCombo(label: str, preview_value: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginDisabled(disabled: bool = True) -> None:
    ...
def BeginGroup() -> None:
    ...
def BeginItemTooltip() -> bool:
    ...
def BeginListBox(label: str, size: Vec2 = ...) -> bool:
    ...
def BeginMainMenuBar() -> bool:
    ...
def BeginMenu(label: str, enabled: bool = True) -> bool:
    ...
def BeginMenuBar() -> bool:
    ...
def BeginPopup(str_id: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginPopupContextItem(str_id: str = None, popup_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginPopupContextVoid(str_id: str = None, popup_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginPopupContextWindow(str_id: str = None, popup_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginPopupModal(name: str, p_open: bool = None, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, bool]:
    ...
def BeginTabBar(str_id: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
@typing.overload
def BeginTabItem(label: str, p_open: bool, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, bool]:
    ...
@typing.overload
def BeginTabItem(label: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def BeginTable(str_id: str, columns: typing.SupportsInt | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0, outer_size: Vec2 = ..., inner_width: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> bool:
    ...
def BeginTooltip() -> bool:
    ...
def Bullet() -> None:
    ...
def BulletText(txt: str) -> None:
    ...
def Button(label: str, size: Vec2 = ...) -> bool:
    ...
def CalcItemWidth() -> float:
    ...
def CalcTextSize(text: str, text_end: str = None, hide_text_after_double_hash: bool = False, wrap_width: typing.SupportsFloat | typing.SupportsIndex = -1.0) -> Vec2:
    ...
def Checkbox(label: str, v: bool) -> tuple[bool, bool]:
    ...
def CloseCurrentPopup() -> None:
    ...
def CollapsingHeader(label: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def CollapsingHeader2(label: str, p_visible: bool, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, bool]:
    ...
def ColorButton(desc_id: str, col: Vec4, flags: typing.SupportsInt | typing.SupportsIndex = 0, size: Vec2 = ...) -> bool:
    ...
def ColorConvertFloat4ToU32(in: Vec4) -> int:
    ...
def ColorConvertHSVtoRGB(h: typing.SupportsFloat | typing.SupportsIndex, s: typing.SupportsFloat | typing.SupportsIndex, v: typing.SupportsFloat | typing.SupportsIndex, out_r: typing.SupportsFloat | typing.SupportsIndex, out_g: typing.SupportsFloat | typing.SupportsIndex, out_b: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def ColorConvertRGBtoHSV(r: typing.SupportsFloat | typing.SupportsIndex, g: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, out_h: typing.SupportsFloat | typing.SupportsIndex, out_s: typing.SupportsFloat | typing.SupportsIndex, out_v: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def ColorConvertU32ToFloat4(in: typing.SupportsInt | typing.SupportsIndex) -> Vec4:
    ...
def ColorEdit3(label: str, col: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[float]]:
    ...
def ColorEdit4(label: str, col: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[float]]:
    ...
def ColorPicker3(label: str, col: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[float]]:
    ...
def ColorPicker4(label: str, col: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0, ref_col: typing.SupportsFloat | typing.SupportsIndex = None) -> tuple[bool, list[float]]:
    ...
def Columns(count: typing.SupportsInt | typing.SupportsIndex = 1, id: str = None, border: bool = True) -> None:
    ...
def Combo(label: str, current_item: typing.SupportsInt | typing.SupportsIndex, items: collections.abc.Sequence[str], popup_max_height_in_items: typing.SupportsInt | typing.SupportsIndex = -1) -> tuple[bool, int]:
    ...
def ComboStr(label: str, current_item: typing.SupportsInt | typing.SupportsIndex, items_separated_by_zeros: str, popup_max_height_in_items: typing.SupportsInt | typing.SupportsIndex = -1) -> tuple[bool, int]:
    ...
def CreateContext() -> int:
    """
    Creates a context and makes it current; returns its handle.
    """
def DestroyContext(ptr: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    """
    Destroys the given context (0: the current one).
    """
def DockBuilderAddNode(node_id: typing.SupportsInt | typing.SupportsIndex = 0, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> int:
    ...
def DockBuilderDockWindow(window_name: str, node_id: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def DockBuilderFinish(node_id: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def DockBuilderGetNode(node_id: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def DockBuilderRemoveNode(node_id: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def DockBuilderSetNodeSize(node_id: typing.SupportsInt | typing.SupportsIndex, size: Vec2) -> None:
    ...
def DockBuilderSplitNode(id: typing.SupportsInt | typing.SupportsIndex, split_dir: Dir, size_ratio_for_node_at_dir: typing.SupportsFloat | typing.SupportsIndex) -> tuple[int, int]:
    ...
def DockSpace(id: typing.SupportsInt | typing.SupportsIndex, size: Vec2 = ..., flags: typing.SupportsInt | typing.SupportsIndex = 0) -> int:
    ...
def DockSpaceOverMainViewport(id: typing.SupportsInt | typing.SupportsIndex = 0, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> int:
    ...
def DragFloat(label: str, v: typing.SupportsFloat | typing.SupportsIndex, v_speed: typing.SupportsFloat | typing.SupportsIndex = 1.0, v_min: typing.SupportsFloat | typing.SupportsIndex = 0.0, v_max: typing.SupportsFloat | typing.SupportsIndex = 0.0, format: str = '%.3f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, float]:
    ...
def DragFloatN(label: str, v: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], v_speed: typing.SupportsFloat | typing.SupportsIndex = 1.0, v_min: typing.SupportsFloat | typing.SupportsIndex = 0.0, v_max: typing.SupportsFloat | typing.SupportsIndex = 0.0, format: str = '%.3f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[float]]:
    ...
def DragInt(label: str, v: typing.SupportsInt | typing.SupportsIndex, v_speed: typing.SupportsFloat | typing.SupportsIndex = 1.0, v_min: typing.SupportsInt | typing.SupportsIndex = 0, v_max: typing.SupportsInt | typing.SupportsIndex = 0, format: str = '%d', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, int]:
    ...
def DragIntN(label: str, v: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], v_speed: typing.SupportsFloat | typing.SupportsIndex = 1.0, v_min: typing.SupportsInt | typing.SupportsIndex = 0, v_max: typing.SupportsInt | typing.SupportsIndex = 0, format: str = '%d', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[int]]:
    ...
def Dummy(size: Vec2) -> None:
    ...
def End() -> None:
    ...
def EndChild() -> None:
    ...
def EndCombo() -> None:
    ...
def EndDisabled() -> None:
    ...
def EndFrame() -> None:
    ...
def EndGroup() -> None:
    ...
def EndListBox() -> None:
    ...
def EndMainMenuBar() -> None:
    ...
def EndMenu() -> None:
    ...
def EndMenuBar() -> None:
    ...
def EndPopup() -> None:
    ...
def EndTabBar() -> None:
    ...
def EndTabItem() -> None:
    ...
def EndTable() -> None:
    ...
def EndTooltip() -> None:
    ...
def GetBackgroundDrawList() -> DrawList:
    ...
def GetClipboardText() -> str:
    ...
@typing.overload
def GetColorU32(idx: typing.SupportsInt | typing.SupportsIndex, alpha_mul: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> int:
    ...
@typing.overload
def GetColorU32(col: Vec4) -> int:
    ...
@typing.overload
def GetColorU32(col: typing.SupportsInt | typing.SupportsIndex, alpha_mul: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> int:
    ...
def GetColumnIndex() -> int:
    ...
def GetColumnOffset(column_index: typing.SupportsInt | typing.SupportsIndex = -1) -> float:
    ...
def GetColumnWidth(column_index: typing.SupportsInt | typing.SupportsIndex = -1) -> float:
    ...
def GetColumnsCount() -> int:
    ...
def GetContentRegionAvail() -> Vec2:
    ...
def GetContentRegionMax() -> Vec2:
    ...
def GetCurrentContext() -> int:
    ...
def GetCursorPos() -> Vec2:
    ...
def GetCursorPosX() -> float:
    ...
def GetCursorPosY() -> float:
    ...
def GetCursorScreenPos() -> Vec2:
    ...
def GetCursorStartPos() -> Vec2:
    ...
def GetFontSize() -> float:
    ...
def GetFontTexUvWhitePixel() -> Vec2:
    ...
def GetForegroundDrawList() -> DrawList:
    ...
def GetFrameCount() -> int:
    ...
def GetFrameHeight() -> float:
    ...
def GetFrameHeightWithSpacing() -> float:
    ...
@typing.overload
def GetID(str_id: str) -> int:
    ...
@typing.overload
def GetID(str_id_begin: str, str_id_end: str) -> int:
    ...
def GetIO() -> IO:
    ...
def GetItemID() -> int:
    ...
def GetItemRectMax() -> Vec2:
    ...
def GetItemRectMin() -> Vec2:
    ...
def GetItemRectSize() -> Vec2:
    ...
def GetKeyName(key: Key) -> str:
    ...
def GetKeyPressedAmount(key: Key, repeat_delay: typing.SupportsFloat | typing.SupportsIndex, rate: typing.SupportsFloat | typing.SupportsIndex) -> int:
    ...
def GetMouseClickedCount(button: typing.SupportsInt | typing.SupportsIndex) -> int:
    ...
def GetMouseCursor() -> int:
    ...
def GetMouseDragDelta(button: typing.SupportsInt | typing.SupportsIndex = 0, lock_threshold: typing.SupportsFloat | typing.SupportsIndex = -1.0) -> Vec2:
    ...
def GetMousePos() -> Vec2:
    ...
def GetMousePosOnOpeningCurrentPopup() -> Vec2:
    ...
def GetScrollMaxX() -> float:
    ...
def GetScrollMaxY() -> float:
    ...
def GetScrollX() -> float:
    ...
def GetScrollY() -> float:
    ...
def GetStyle() -> Style:
    ...
def GetStyleColorVec4(idx: typing.SupportsInt | typing.SupportsIndex) -> Vec4:
    ...
def GetTextLineHeight() -> float:
    ...
def GetTextLineHeightWithSpacing() -> float:
    ...
def GetTime() -> float:
    ...
def GetTreeNodeToLabelSpacing() -> float:
    ...
def GetWindowContentRegionMax() -> Vec2:
    ...
def GetWindowContentRegionMin() -> Vec2:
    ...
def GetWindowDockID() -> int:
    ...
def GetWindowDpiScale() -> float:
    ...
def GetWindowDrawList() -> DrawList:
    ...
def GetWindowHeight() -> float:
    ...
def GetWindowPos() -> Vec2:
    ...
def GetWindowSize() -> Vec2:
    ...
def GetWindowWidth() -> float:
    ...
def Image(user_texture_id: typing.SupportsInt | typing.SupportsIndex, image_size: Vec2, uv0: Vec2 = ..., uv1: Vec2 = ..., tint_col: Vec4 = ..., border_col: Vec4 = ...) -> None:
    ...
def ImageButton(str_id: str, user_texture_id: typing.SupportsInt | typing.SupportsIndex, image_size: Vec2, uv0: Vec2 = ..., uv1: Vec2 = ..., bg_col: Vec4 = ..., tint_col: Vec4 = ...) -> bool:
    ...
def Indent(indent_w: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
    ...
def InputDouble(label: str, v: typing.SupportsFloat | typing.SupportsIndex, step: typing.SupportsFloat | typing.SupportsIndex = 0.0, step_fast: typing.SupportsFloat | typing.SupportsIndex = 0.0, format: str = '%.6f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, float]:
    ...
def InputFloat(label: str, v: typing.SupportsFloat | typing.SupportsIndex, step: typing.SupportsFloat | typing.SupportsIndex = 0.0, step_fast: typing.SupportsFloat | typing.SupportsIndex = 0.0, format: str = '%.3f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, float]:
    ...
def InputFloatN(label: str, v: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], format: str = '%.3f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[float]]:
    ...
def InputInt(label: str, v: typing.SupportsInt | typing.SupportsIndex, step: typing.SupportsInt | typing.SupportsIndex = 1, step_fast: typing.SupportsInt | typing.SupportsIndex = 100, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, int]:
    ...
def InputIntN(label: str, v: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[int]]:
    ...
def InputText(label: str, text: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, str]:
    ...
def InputTextMultiline(label: str, text: str, size: Vec2 = ..., flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, str]:
    ...
def InputTextWithHint(label: str, hint: str, text: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, str]:
    ...
def InvisibleButton(str_id: str, size: Vec2, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def IsAnyItemActive() -> bool:
    ...
def IsAnyItemFocused() -> bool:
    ...
def IsAnyItemHovered() -> bool:
    ...
def IsAnyMouseDown() -> bool:
    ...
def IsItemActivated() -> bool:
    ...
def IsItemActive() -> bool:
    ...
def IsItemClicked(mouse_button: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def IsItemDeactivated() -> bool:
    ...
def IsItemDeactivatedAfterEdit() -> bool:
    ...
def IsItemEdited() -> bool:
    ...
def IsItemFocused() -> bool:
    ...
def IsItemHovered(flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def IsItemToggledOpen() -> bool:
    ...
def IsItemVisible() -> bool:
    ...
def IsKeyChordPressed(key_chord: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def IsKeyDown(key: Key) -> bool:
    ...
def IsKeyPressed(key: Key, repeat: bool = True) -> bool:
    ...
def IsKeyReleased(key: Key) -> bool:
    ...
def IsMouseClicked(button: typing.SupportsInt | typing.SupportsIndex, repeat: bool = False) -> bool:
    ...
def IsMouseDoubleClicked(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def IsMouseDown(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def IsMouseDragging(button: typing.SupportsInt | typing.SupportsIndex, lock_threshold: typing.SupportsFloat | typing.SupportsIndex = -1.0) -> bool:
    ...
def IsMouseHoveringRect(r_min: Vec2, r_max: Vec2, clip: bool = True) -> bool:
    ...
def IsMousePosValid(mouse_pos: Vec2 = None) -> bool:
    ...
def IsMouseReleased(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def IsPopupOpen(str_id: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
@typing.overload
def IsRectVisible(size: Vec2) -> bool:
    ...
@typing.overload
def IsRectVisible(rect_min: Vec2, rect_max: Vec2) -> bool:
    ...
def IsWindowAppearing() -> bool:
    ...
def IsWindowCollapsed() -> bool:
    ...
def IsWindowDocked() -> bool:
    ...
def IsWindowFocused(flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def IsWindowHovered(flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def LabelText(label: str, txt: str) -> None:
    ...
@typing.overload
def MenuItem(label: str, shortcut: str = None, selected: bool = False, enabled: bool = True) -> bool:
    ...
@typing.overload
def MenuItem(label: str, shortcut: str, p_selected: bool, enabled: bool = True) -> tuple[bool, bool]:
    ...
def NewFrame() -> None:
    ...
def NewLine() -> None:
    ...
def NextColumn() -> None:
    ...
@typing.overload
def OpenPopup(str_id: str, popup_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
@typing.overload
def OpenPopup(id: typing.SupportsInt | typing.SupportsIndex, popup_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def OpenPopupOnItemClick(str_id: str = None, popup_flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def PopButtonRepeat() -> None:
    ...
def PopClipRect() -> None:
    ...
def PopFont() -> None:
    ...
def PopID() -> None:
    ...
def PopItemWidth() -> None:
    ...
def PopStyleColor(count: typing.SupportsInt | typing.SupportsIndex = 1) -> None:
    ...
def PopStyleVar(count: typing.SupportsInt | typing.SupportsIndex = 1) -> None:
    ...
def PopTabStop() -> None:
    ...
def PopTextWrapPos() -> None:
    ...
def ProgressBar(fraction: typing.SupportsFloat | typing.SupportsIndex, size_arg: Vec2 = ..., overlay: str = None) -> None:
    ...
def PushButtonRepeat(repeat: bool) -> None:
    ...
def PushClipRect(clip_rect_min: Vec2, clip_rect_max: Vec2, intersect_with_current_clip_rect: bool) -> None:
    ...
def PushFont(font: Font, font_size_base_unscaled: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
    ...
@typing.overload
def PushID(str_id: str) -> None:
    ...
@typing.overload
def PushID(str_id_begin: str, str_id_end: str) -> None:
    ...
@typing.overload
def PushID(int_id: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def PushItemWidth(item_width: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
@typing.overload
def PushStyleColor(idx: typing.SupportsInt | typing.SupportsIndex, col: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
@typing.overload
def PushStyleColor(idx: typing.SupportsInt | typing.SupportsIndex, col: Vec4) -> None:
    ...
@typing.overload
def PushStyleVar(idx: typing.SupportsInt | typing.SupportsIndex, val: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
@typing.overload
def PushStyleVar(idx: typing.SupportsInt | typing.SupportsIndex, val: Vec2) -> None:
    ...
def PushTabStop(tab_stop: bool) -> None:
    ...
def PushTextWrapPos(wrap_local_pos_x: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
    ...
def RadioButton(label: str, active: bool) -> bool:
    ...
def Render() -> None:
    ...
def ResetMouseDragDelta(button: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SameLine(offset_from_start_x: typing.SupportsFloat | typing.SupportsIndex = 0.0, spacing: typing.SupportsFloat | typing.SupportsIndex = -1.0) -> None:
    ...
def Selectable(label: str, selected: bool = False, flags: typing.SupportsInt | typing.SupportsIndex = 0, size: Vec2 = ...) -> bool:
    ...
def Selectable2(label: str, p_selected: bool, flags: typing.SupportsInt | typing.SupportsIndex = 0, size: Vec2 = ...) -> tuple[bool, bool]:
    ...
def Separator() -> None:
    ...
def SeparatorText(label: str) -> None:
    ...
def SetClipboardText(text: str) -> None:
    ...
def SetColorEditOptions(flags: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetColumnOffset(column_index: typing.SupportsInt | typing.SupportsIndex, offset_x: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetColumnWidth(column_index: typing.SupportsInt | typing.SupportsIndex, width: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetCurrentContext(arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetCursorPos(local_pos: Vec2) -> None:
    ...
def SetCursorPosX(local_x: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetCursorPosY(local_y: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetCursorScreenPos(pos: Vec2) -> None:
    ...
def SetItemDefaultFocus() -> None:
    ...
def SetItemTooltip(txt: str) -> None:
    ...
def SetKeyboardFocusHere(offset: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetMouseCursor(cursor_type: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetNextFrameWantCaptureKeyboard(want_capture_keyboard: bool) -> None:
    ...
def SetNextFrameWantCaptureMouse(want_capture_mouse: bool) -> None:
    ...
def SetNextItemAllowOverlap() -> None:
    ...
def SetNextItemOpen(is_open: bool, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetNextItemShortcut(key_chord: typing.SupportsInt | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetNextItemWidth(item_width: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetNextWindowBgAlpha(alpha: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetNextWindowCollapsed(collapsed: bool, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetNextWindowContentSize(size: Vec2) -> None:
    ...
def SetNextWindowDockID(dock_id: typing.SupportsInt | typing.SupportsIndex, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetNextWindowFocus() -> None:
    ...
def SetNextWindowPos(pos: Vec2, cond: typing.SupportsInt | typing.SupportsIndex = 0, pivot: Vec2 = ...) -> None:
    ...
def SetNextWindowScroll(scroll: Vec2) -> None:
    ...
def SetNextWindowSize(size: Vec2, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def SetNextWindowSizeConstraints(size_min: Vec2, size_max: Vec2) -> None:
    ...
def SetNextWindowViewport(viewport_id: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def SetScrollFromPosX(local_x: typing.SupportsFloat | typing.SupportsIndex, center_x_ratio: typing.SupportsFloat | typing.SupportsIndex = 0.5) -> None:
    ...
def SetScrollFromPosY(local_y: typing.SupportsFloat | typing.SupportsIndex, center_y_ratio: typing.SupportsFloat | typing.SupportsIndex = 0.5) -> None:
    ...
def SetScrollHereX(center_x_ratio: typing.SupportsFloat | typing.SupportsIndex = 0.5) -> None:
    ...
def SetScrollHereY(center_y_ratio: typing.SupportsFloat | typing.SupportsIndex = 0.5) -> None:
    ...
def SetScrollX(scroll_x: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetScrollY(scroll_y: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
def SetTabItemClosed(tab_or_docked_window_label: str) -> None:
    ...
def SetTooltip(txt: str) -> None:
    ...
@typing.overload
def SetWindowCollapsed(collapsed: bool, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def SetWindowCollapsed(name: str, collapsed: bool, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def SetWindowFocus() -> None:
    ...
@typing.overload
def SetWindowFocus(name: str) -> None:
    ...
def SetWindowFontScale(scale: typing.SupportsFloat | typing.SupportsIndex) -> None:
    ...
@typing.overload
def SetWindowPos(pos: Vec2, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def SetWindowPos(name: str, pos: Vec2, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def SetWindowSize(size: Vec2, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
@typing.overload
def SetWindowSize(name: str, size: Vec2, cond: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def Shortcut(key_chord: typing.SupportsInt | typing.SupportsIndex, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def ShowDemoWindow() -> bool:
    ...
def SliderAngle(label: str, v_rad: typing.SupportsFloat | typing.SupportsIndex, v_degrees_min: typing.SupportsFloat | typing.SupportsIndex = -360.0, v_degrees_max: typing.SupportsFloat | typing.SupportsIndex = 360.0, format: str = '%.0f deg', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, float]:
    ...
def SliderFloat(label: str, v: typing.SupportsFloat | typing.SupportsIndex, v_min: typing.SupportsFloat | typing.SupportsIndex, v_max: typing.SupportsFloat | typing.SupportsIndex, format: str = '%.3f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, float]:
    ...
def SliderFloatN(label: str, v: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], v_min: typing.SupportsFloat | typing.SupportsIndex, v_max: typing.SupportsFloat | typing.SupportsIndex, format: str = '%.3f', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[float]]:
    ...
def SliderInt(label: str, v: typing.SupportsInt | typing.SupportsIndex, v_min: typing.SupportsInt | typing.SupportsIndex, v_max: typing.SupportsInt | typing.SupportsIndex, format: str = '%d', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, int]:
    ...
def SliderIntN(label: str, v: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], v_min: typing.SupportsInt | typing.SupportsIndex, v_max: typing.SupportsInt | typing.SupportsIndex, format: str = '%d', flags: typing.SupportsInt | typing.SupportsIndex = 0) -> tuple[bool, list[int]]:
    ...
def SmallButton(label: str) -> bool:
    ...
def Spacing() -> None:
    ...
def StyleColorsClassic(dst: Style = None) -> None:
    ...
def StyleColorsDark(dst: Style = None) -> None:
    ...
def StyleColorsLight(dst: Style = None) -> None:
    ...
def TabItemButton(label: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
def TableAngledHeadersRow() -> None:
    ...
def TableGetColumnCount() -> int:
    ...
def TableGetColumnFlags(column_n: typing.SupportsInt | typing.SupportsIndex = -1) -> int:
    ...
def TableGetColumnIndex() -> int:
    ...
def TableGetColumnName(column_n: typing.SupportsInt | typing.SupportsIndex = -1) -> str:
    ...
def TableGetHoveredColumn() -> int:
    ...
def TableGetRowIndex() -> int:
    ...
def TableHeader(label: str) -> None:
    ...
def TableHeadersRow() -> None:
    ...
def TableNextColumn() -> bool:
    ...
def TableNextRow(row_flags: typing.SupportsInt | typing.SupportsIndex = 0, min_row_height: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
    ...
def TableSetBgColor(target: typing.SupportsInt | typing.SupportsIndex, color: typing.SupportsInt | typing.SupportsIndex, column_n: typing.SupportsInt | typing.SupportsIndex = -1) -> None:
    ...
def TableSetColumnEnabled(column_n: typing.SupportsInt | typing.SupportsIndex, v: bool) -> None:
    ...
def TableSetColumnIndex(column_n: typing.SupportsInt | typing.SupportsIndex) -> bool:
    ...
def TableSetupColumn(label: str, flags: typing.SupportsInt | typing.SupportsIndex = 0, init_width_or_weight: typing.SupportsFloat | typing.SupportsIndex = 0.0, user_id: typing.SupportsInt | typing.SupportsIndex = 0) -> None:
    ...
def TableSetupScrollFreeze(cols: typing.SupportsInt | typing.SupportsIndex, rows: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
def Text(txt: str) -> None:
    ...
def TextColored(col: Vec4, txt: str) -> None:
    ...
def TextDisabled(txt: str) -> None:
    ...
def TextLink(label: str) -> bool:
    ...
def TextLinkOpenURL(label: str, url: str = None) -> bool:
    ...
def TextUnformatted(txt: str) -> None:
    ...
def TextWrapped(txt: str) -> None:
    ...
@typing.overload
def TreeNode(label: str) -> bool:
    ...
@typing.overload
def TreeNode(str_id: str, txt: str) -> bool:
    ...
@typing.overload
def TreeNodeEx(label: str, flags: typing.SupportsInt | typing.SupportsIndex = 0) -> bool:
    ...
@typing.overload
def TreeNodeEx(str_id: str, flags: typing.SupportsInt | typing.SupportsIndex, txt: str) -> bool:
    ...
def TreePop() -> None:
    ...
def TreePush(str_id: str) -> None:
    ...
def Unindent(indent_w: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
    ...
@typing.overload
def Value(prefix: str, b: bool) -> None:
    ...
@typing.overload
def Value(prefix: str, v: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
@typing.overload
def Value(prefix: str, v: typing.SupportsInt | typing.SupportsIndex) -> None:
    ...
@typing.overload
def Value(prefix: str, v: typing.SupportsFloat | typing.SupportsIndex, float_format: str = None) -> None:
    ...
