# OCX_Schema: Changelog

## 3.0.0_alpha 2023.07.10

release tag: 

### Issues solved

### Changed
  - Delete ``SchemaChange`` documentation as we have converted to this ``CHANGELOG.md``
  - Remove ``substitutionGroup`` from ``entityRefBase`` and ``BoundedRef``
  - Add ``Hole2DContour`` to ``refType``
  - Made ``FlangeWidth`` optional on ``BulbFlat`` element.  (oca) ([#7](https://github.com/OCXStandard/OCX_Schema/issues/7))
  - Rename ``functionType`` enumerator: ``DECK: Weateher deck -> DECK: Weather deck``. (oca)  ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename ``functionType`` enumerator: ``DECK: Tweeen deck -> DECK: Tween deck``.  (oca)  ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename ``functionType`` enumerator: ``DECK: DECK: Weelhouse deck -> DECK: Wheelhouse deck``.  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename attribute ``lenghtClass->lengthClass``.  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename attribute of element ``XRefPlanes``:  ``isReveresed -> isReversed``  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename ``PentetratingObject_T -> PenetratingObject_T``.  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename  ``liquidCargoType`` enumerator: ``chemichal -> chemical``.  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename  ``liquidCargoType`` enumerator: ``hydroclorid acid -> hydrochloride acid lubricationg oil -> lubricating oil``.  (oca)  ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16)) 
  - Rename  ``liquidCargoType`` enumerator: ``lubricationg oil -> lubricating oil``.  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename ``gaseousCargoType`` enumerator: ``liquified natural gas->liquefied natural gas ``.  (oca)  ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename ``gaseousCargoType`` enumerator: ``liquified petroleum gas -> liquefied petroleum gas``.  (oca)  ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
  - Rename ``itemRef`` enumerator: ``OccurenceGroup -> OccurrenceGroup``.  (oca)   ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))
### Added
  - Include boilerplate Apache 2.0 license information to the ``Header`` attribute: ``license``.  (oca)  
### Fixed

  - Several typos in the schema annotation strings.  (oca) ([#16](https://github.com/OCXStandard/OCX_Schema/issues/16))

## 2.8.6_fix - 2022-10-06 
Release tag: [v2.8.6](https://github.com/OCXStandard/OCX_Schema/releases/tag/v2.8.6_fix)


### Changed
  - Added the ``UnboundedGeometry`` tag to ``CompartmentFace``.  (oca)  ([#3](https://github.com/OCXStandard/OCX_Schema/issues/3))
## 2.8.6 - 2021-06-10
Release tag: [v2.8.6](https://github.com/OCXStandard/OCX_Schema/releases/tag/v2.8.6)

### Added

  - Add the attribute ``isUVspace``. The exporting application may set this attribute to true and provide the ``FreeEdgeCoordinates`` UV coordinates. This will only be relevant for NURBS3D curves.  (oca)  ``FreeEdgeCurve``
  - Add a new type ``LONGITUDINAL: Top tank``.  (oca)  ``functionType``
  - Add ``EdgeReinforcement`` entity used for describing edge reinforcements of free edges.  (oca)  ``EdgeReinforcement``
  - Add the ``EdgeReinforcement`` entity. (oca)  ``StiffenedBy``
  - Add ``TraceLine``.  (oca)  ``EdgeReinforcement``
  - Add ``ChildRef`` to occurrence group.  (oca)  ``EntityRefBase``
  - Add missing mandatory attribute ``refType``..  (oca)  ``RootRef``
  - Add a new ``ZGrid`` concept which defines the grid positions of the vessel along the Z axis.  (oca)  ``ZGrid``
  - Add a new ``YGrid`` concept which defines the grid positions of the vessel along the Y axis.  (oca)  ``YGrid``
  - Add a new ``XGrid`` representing a frame table concept which is not to be confused with the existing ``FrameTables`` (in plural) entity.The ``XGrid`` is a concept which defines the frame positions of the vessel along the X axis by giving frame number, spacing and count.The purpose of the ``XGrid`` concept is to give a compact definition of the vessel grid system for navigating the 3D model. This concept shall not be used for crating bounds to other objects in ``LimitedBy``.  (oca)  ``XGrid``
  - Add a new ``VesselGrid`` entity which defines a collection of X, Y and Z grid definitions.  (oca)  ``VesselGrid``
  - Add ``EdgeReinforcement`` to enumerator.  (oca)  ``refType``

### Changed
  - Change model to ``Choice[2,2]``. (oca)  ``BoundingBox``
  - Change model to ``Choice[1,1]``.  (oca)  ``BarSection``
  - Change the type ``LONGITUDINAL: Hopper side top tank`` to ``LONGITUDINAL: Hopper side upper``.  (oca)  ``functionType``
  - Change ``LONGITUDINAL: Hopper side bilge`` to ``LONGITUDINAL: Hopper side bottom``.  (oca)  ``functionType``
  - Rename ``FrameSpacingGroup`` to ``XSpacingGroup``.  (oca)  ``XSpacingGroup``
  - Change ``Material`` to ``MaterialRef`` (oca)  ``EdgeReinforcement``
  - Remove ``BoundingBox`` from ``EdgeCurveRef`` and made ``EdgeCurveRef`` unbounded to reference more than one curve.  (oca)  ``EdgeCurveRef``
  - Change ``EntityRefBase_T`` to ``RootRef_T``.  (oca)  ``RootRef``
  - Change supertype from ``EntityBase`` to ``GeometryRepresentation``  (oca)  ``Cell``
  - Remove assertion on ``EntityBase`` as this is not necessary when ``IdBase`` has a mandatory attribute ``id``.  (oca)  ``EntityBase``
  - Rename  ``FrameTable`` to ``XGrid`` for a consistent semantic.  (oca)  ``VesselGrid``
  - Rename ``EdgeReinforcement -> FlangeEdgeReinforcement`` as we now introduced a new ``EdgeReinforcement`` concept..  (oca)  ``BracketParameters``

### Fixed
  - Make ``LimitedBy`` optional.  (oca)  ``Bracket``
  - Typo in the attribute name ``firstGridNumber``.  (oca)  ``XSpacingGroup``
  - Make ``LimitedBy`` optional.  (oca)  ``Pillar``
  - The ``FrameTables`` entity is kept for backward compatibility. It might change in a future schema version..  (oca)  ``CoordinateSystem``
  - Make attribute ``id`` mandatory on all elements inheriting from ``IdBase``.  (oca)  ``IdBase``