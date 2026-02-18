# OCX_Schema: Changelog

All notable changes to the OCX schema will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to the Python [PEP 440 versioning recommendations](https://peps.python.org/pep-0440/).

### Types of changes
* ``Added`` for new features.
* ``Changed`` for changes in existing functionality.
* ``Deprecated`` for soon-to-be removed features.
* ``Removed`` for now removed features.
* ``Fixed`` for any bug fixes.
* ``Security`` in case of vulnerabilities.


## [3.2.0rc8] - 2026.02.18

Bump to 3.2.0rc8 and publish release candidate

### Changed

* [Offset and OffsetDirection missing from in BoundedRef #253](https://github.com/OCXStandard/OCX_Schema/issues/253)

    ** Impact:** Translator change (Re-installed missing Offset and OffsetDirection to BoundedRef accidentally removed in rc7)

### Added

* [Remove mandatory contour bounds for GridRef and SurfaceRef in LimitedBy #254](https://github.com/OCXStandard/OCX_Schema/issues/254)

    **Impact:** Translator change (Added new types UnboundedSurfaceRef and UnboundedGridRef without ContourBounds)


## [3.2.0rc7] - 2026.02.13

Bump to 3.2.0rc7 and publish release candidate

### Changed
* [Fix side effects of issues #172: duplicate Normal on Plane3D #245](https://github.com/OCXStandard/OCX_Schema/issues/245)

     **Impact:** No impact on the translator (removed duplicate Normal and Origin elements from Plane3D)

* [Fix bug introduced in #175: Ellipse is wrongly attributed as an abstract element #247](https://github.com/OCXStandard/OCX_Schema/issues/247)

     **Impact:** No impact on the translator (removed abstract attribute from Ellipse)

* [Add BracketRef to the Penetration #250](https://github.com/OCXStandard/OCX_Schema/issues/250)

     **Impact:** Added BracketRef to Penetration as an optional reference to a bracket.

### Added
* [Make WebStiffenerRef a reference without ContourBounds #248](https://github.com/OCXStandard/OCX_Schema/issues/248)

     **Impact:** Added new element StrWebStiffenerRef without ContourBounds.

* [ContourBounds should not be present in DesignView #249](https://github.com/OCXStandard/OCX_Schema/issues/249)

     **Impact:** Created StrStiffenerRef, StrSeamRef and StrEdgeReinforcement as pure references without ContourBounds.


## [3.2.0rc6] - 2026.02.08

Bump to 3.2.0rc6 and publish release candidate


## [3.2.0rc6] - 2026.02.08
### Changed
* [Wrong naming of MassProperty element #243](https://github.com/OCXStandard/OCX_Schema/issues/243)

    **Impact:** Translator change (Renaming entity from PhysicalMouldedCenterOfGravity to PhysicalCenterOfGravity)


## [3.2.0rc5] - 2026.02.02

Bump to 3.2.0rc5 and publish release candidate


## [3.2.0rc5] - 2026.01.30
### Added
* [Add mounting rule for stiffeners supplementing the Inclination information #238](https://github.com/OCXStandard/OCX_Schema/issues/238)

    **Impact:** No impact on the translator (optional attributes)

* [Add Offset and OffsetDirection to BoundedRef and make them mandatory #241](https://github.com/OCXStandard/OCX_Schema/issues/241)

   **Impact:** Translator change (Mandatory new elements)


## [3.2.0rc4] - 2026.01.19
Bump to 3.2.0rc4 and publish release candidate

## [3.2.0rc4] - 2026.01.19

### Changed
* [PointOnSurface needs to be global and implemented for both Panel and Plate #235](https://github.com/OCXStandard/OCX_Schema/issues/235)

    **Impact:** Translator change (Cardinality change and new optional PointOnSurface element)

## [3.2.0rc3] - 2026.01.08
Bump to 3.2.0rc3 and publish release candidate

## [3.2.0rc3] - 2026.01.08

### Changed
* [Surface and Panel must support multiple outer contours/face boundary curves #233](https://github.com/OCXStandard/OCX_Schema/issues/233)

    **Impact:** Translator change (Cardinality change)

* [StiffenedBy need to support a combination of Stiffener and EdgeReinforcement #200](https://github.com/OCXStandard/OCX_Schema/issues/200)

  **Impact:** Translator change (Cardinality change)

## [3.2.0rc2] - 2026.01.07
Bump to 3.2.0rc2 and publish release candidate

## [3.2.0rc1] - 2026.01.07

### Added

* [Add a reference to the standard profile section at the Bar Section level #226](https://github.com/OCXStandard/OCX_Schema/issues/226)

    **Impact:** None, optional attribute

* [Add Aluminium to the MaterialCatalogue #227](https://github.com/OCXStandard/OCX_Schema/issues/227)

    **Impact:** Translator change: New entity Aluminium.

* [Add voluntary thickness addition for flange and web #9](https://github.com/OCXStandard/OCX_Schema/issues/9)

    **Impact:** None, optional entity

* [Add Support renewal thickness #9](https://github.com/OCXStandard/OCX_Schema/issues/9)
    
    **Impact:** None (optional fields)
* [Add Density to BulkCargo #185](https://github.com/OCXStandard/OCX_Schema/issues/185)
  
    **Impact:** Translator change (mandatory field)
* [Add MinimumBallastDraught to PrincipalParticulars #184](https://github.com/OCXStandard/OCX_Schema/issues/184)
  
    **Impact:** None (optional field)
*  [Add optional volume properties to MassProperties #180](https://github.com/OCXStandard/OCX_Schema/issues/180)

    **Impact:** None (optional fields)
* [Add normal Ellipse to Hole2D catalogue and fix SuperElliptical #175](https://github.com/OCXStandard/OCX_Schema/issues/175)

    **Impact:** Translator change (new catalogue item, attribute name change)
* [Add OTHER to newbuildingSocietyName #166](https://github.com/OCXStandard/OCX_Schema/issues/166)

    **Impact:** Translator change (new enumerator field)

### Changed

* [Panel LimitedBy Ambiguity #192](https://github.com/OCXStandard/OCX_Schema/issues/192)

    **Impact:** Translator change (The definition of the BoundedRef for Panel LimitedBy has changed adding a contour mid-point and a point on the surface)

* [Bulbflat Description #190](https://github.com/OCXStandard/OCX_Schema/issues/190)

    **Impact:** None (Documentation change only)

* [Add mandatory bulb radius, angle, bulb width and height #225](https://github.com/OCXStandard/OCX_Schema/issues/225)

    **Impact:** Translator change (Made FlangeWidth, BulbOuterRadius and BulbAngle mandatory)

* [Rename Material to Steel #227](https://github.com/OCXStandard/OCX_Schema/issues/227)

    **Impact:** Translator change: Material renamed to Steel.

* [Extend ReferenceSurfaces to allow for a combination of Surface and SurfaceCollection #201](https://github.com/OCXStandard/OCX_Schema/issues/201)

    **Impact:** None (only impact validation)

* [Add strict formatting of GUID #199](https://github.com/OCXStandard/OCX_Schema/issues/199)

    **Impact:** None (GUID format validation)

* [Material grade aligned with IACS Unified Requirements S6 “Use of Steel Grades for Various Hull Members – Ships of 90m in Length and Above – Rev.9 Corr.2 Nov 2021” Table 7 #182](https://github.com/OCXStandard/OCX_Schema/issues/182)
  
    **Impact:** Translator change (new enumerator fields)
* [Change LBarOF local properties to reference global properties #189](https://github.com/OCXStandard/OCX_Schema/issues/189)

    **Impact:** None
* [Make FlangeDirection mandatory for Inclination #196](https://github.com/OCXStandard/OCX_Schema/issues/196)

    **Impact:** Translator change (mandatory field)
* [Make RectangularMickeyMouseEars  part of the ParametricHole2D substitution group #174](https://github.com/OCXStandard/OCX_Schema/issues/174)

    **Impact:** Translator change (new substitution item)
* [Change RoundBar Height to Diameter #177](https://github.com/OCXStandard/OCX_Schema/issues/177)

    **Impact:** Translator change (attribute name change)
* [Document Plane3D attributes #80](https://github.com/OCXStandard/OCX_Schema/issues/80)

    **Impact:** None (documentation only)

### Removed
* [Material has been replaced by Steel #227](https://github.com/OCXStandard/OCX_Schema/issues/227)
  
   **Impact:** Translator change (new element and name change)

* [PhysicalProperties has been replaced by MassProperties #180](https://github.com/OCXStandard/OCX_Schema/issues/180)

    **Impact:** Translator change (new element and name change)
    
* [DryWeight has been replaced with MouldedDryWeight #180](https://github.com/OCXStandard/OCX_Schema/issues/180)

    **Impact:** Translator change (name change)
* [CenterOfGravity has been replaced with MouldedCenterOfGravity #180](https://github.com/OCXStandard/OCX_Schema/issues/180)

    **Impact:** Translator change (name change)
* [Delete WebStiffenerRef_T as it is not used #170](https://github.com/OCXStandard/OCX_Schema/issues/170)

    **Impact:** None

### Deprecated
* [SuperElliptical will be removed from the schema in a future release and is replaced by Ellipse #175](https://github.com/OCXStandard/OCX_Schema/issues/175)

## [3.1.0] - 2025.05.15

Bump to 3.1.0
Release tag: [v3.1.0](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.1.0)

## [3.1.0rc4] - 2025.03.07
### Schema release candidate

Bump to 3.1.0rc4

Release tag: [v3.1.0rc4](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.01.0rc4)


### Changed
* [Error in VesselRef and StiffenerRef: Missing mandatory GUIDRef #168](https://github.com/OCXStandard/OCX_Schema/issues/168)


## [3.1.0rc3] - 2025.01.16
### Schema release candidate

Bump to 3.1.0rc3

Release tag: [v3.1.0rc3](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.01.0rc3)


### Changed
* [compartmentPurpose is missing purposes #147](https://github.com/OCXStandard/OCX_Schema/issues/147)
* [Add a boolean to RefPlane to say if it is part of the vessel display grid #160](https://github.com/OCXStandard/OCX_Schema/issues/160)
* [HalfRoundBar schema is inconsistent with respect to the attributes "Height" and "Width" #157](https://github.com/OCXStandard/OCX_Schema/issues/157)
* [EdgeReinforcement on edges defined by GridRef bounds are not supported in schema 3.0.0/3.0.1 #156](https://github.com/OCXStandard/OCX_Schema/issues/156)

### Fixed
* [Documentation of EnumeratedRootUnit:prefix is wrong #141](https://github.com/OCXStandard/OCX_Schema/issues/141)


## [3.1.0rc1] - 2025.01.03
### Schema release candidate

Bump to 3.1.0rc1

Release tag: [v3.1.0rc1](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.01.0rc1)


### Changed
* [EdgeReinforcement on edges defined by GridRef bounds are not supported in schema 3.0.0/3.0.1 #156](https://github.com/OCXStandard/OCX_Schema/issues/156)
* [Consistency of GUIDRef/id between reference and referenced #154](https://github.com/OCXStandard/OCX_Schema/issues/154)

### Fixed
* [Add Hole Curve Reference for EdgeReinforcements #145](https://github.com/OCXStandard/OCX_Schema/issues/145)

## [3.0.1] - 2024.06.20
Bump to 3.0.1

Release tag: [v3.0.1](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.1)

Schema release version

### Changed
* [Wrong cardinality on PlateCutBy #148](https://github.com/OCXStandard/OCX_Schema/issues/148)

Committed missing changes in previous commits:
* [ReferenceBase_T: remove mandatory name attribute #144](https://github.com/OCXStandard/OCX_Schema/issues/144)
* [ConnectedBracketRef_T missing its ref. #123](https://github.com/OCXStandard/OCX_Schema/issues/123)


## [3.0.0] - 2024.04.22
Bump to 3.0.0

Release tag: [v3.0.0](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0)

Schema release version

## [3.0.0rc8] - 2024.04.16
Bump to 3.0.0rc8

Release tag: [v3.0.0rc8](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc8)

Release candidate for version 3.0.0

### Change
* [Add missing EdgeReinforcementRef to LimitedBy #139](https://github.com/OCXStandard/OCX_Schema/issues/139)



## [3.0.0rc7] - 2024.04.09
Bump to 3.0.0rc7

Release tag: [v3.0.0rc7](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc7)

Release candidate for version 3.0.0

### Changed
* [Add type to Occurrence and OccurrenceGroup attribute "type" #137](https://github.com/OCXStandard/OCX_Schema/issues/137)


## [3.0.0rc6] - 2024.04.04
Bump to 3.0.0rc6

Release tag: [v3.0.0rc6](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc6)

Release candidate for version 3.0.0

### Changed
* [Add Occurrence attribute id, nam and type #133](https://github.com/OCXStandard/OCX_Schema/issues/133)


## [3.0.0rc5] - 2024.03.22
Bump to 3.0.0rc5

Release tag: [v3.0.0rc5](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc5)

Release candidate for version 3.0.0

### Changed
* [Positions #130](https://github.com/OCXStandard/OCX_Schema/issues/130)
* [Get rid of OpenCurve/ClosedCurve #129](https://github.com/OCXStandard/OCX_Schema/issues/129)
* [Simplify ocx:NURBS3D's and ocx:NURBSSurface control point representation #128](https://github.com/OCXStandard/OCX_Schema/issues/128)


## [3.0.0rc4] - 2024.03.11
Bump to 3.0.0rc34

Release tag: [v3.0.0rc4](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc4)

Release candidate #3 for version 3.0.0

### Changed
* Downgrade databinding to Python 3.10

## [3.0.0rc3] - 2024.03.08
Bump to 3.0.0rc3

Release tag: [v3.0.0rc3](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc3)

Release candidate #3 for version 3.0.0

### Fixed
 * [ExtrudedSurface require both SweeCurve AND Sweep #125](https://github.com/OCXStandard/OCX_Schema/issues/125)
 * [ConnectedBracketRef_T missing its ref. #123](https://github.com/OCXStandard/OCX_Schema/issues/123)
 * [Enum encoding error for classification society name #122](https://github.com/OCXStandard/OCX_Schema/issues/122)

## [3.0.0rc2] - 2024.03.01
Bump to 3.0.0rc2

Release tag: [v3.0.0rc2](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc2)

Release candidate 2 for version 3.0.0

### Fixed

* [Inclination is unary, but shall be unbounded #115](https://github.com/OCXStandard/OCX_Schema/issues/115)
* [PlateCutBY has no type #116](https://github.com/OCXStandard/OCX_Schema/issues/116)
* [Change FreeEdgeCurve3D to be a choice between a CompositeCurve3D or a ClosedCurve #117](https://github.com/OCXStandard/OCX_Schema/issues/117)
* [Fix wrong format on OCX date items and refType on EdgeCurveRef #120](https://github.com/OCXStandard/OCX_Schema/issues/120)


## [3.0.0rc1] - 2024.02.28
Bump to 3.0.0rc1

Release tag: [v3.0.0rc1](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0rc1)

Release candidate 1 for version 3.0.0

### Fixed
* [Add type to Occurrence #98](https://github.com/OCXStandard/OCX_Schema/issues/98)
* [CellBoundary does not hav a refType #100](https://github.com/OCXStandard/OCX_Schema/issues/100)
* [Make SurfaceCollection unbounded #102](https://github.com/OCXStandard/OCX_Schema/issues/102)
* [Wrong cardinality on curves in CompositeCurve3D #103](https://github.com/OCXStandard/OCX_Schema/issues/103)
* [Remove SlotContour from Panel #109](https://github.com/OCXStandard/OCX_Schema/issues/109)

### Changed
* [Modify TraceLine and OuterContour to reflect the change of CompositeCurve3D #105](https://github.com/OCXStandard/OCX_Schema/issues/105)
* [Add SeamRef and HoleRef to Occurrence #107](https://github.com/OCXStandard/OCX_Schema/issues/107)
* [Make catalogue items to have a mandatory name #111](https://github.com/OCXStandard/OCX_Schema/issues/111)
* [Change UserDefinedBarSection to use CustomProperty #113](https://github.com/OCXStandard/OCX_Schema/issues/113)

## [3.0.0b7] - 2024.02.16
Release tag: [v3.0.0b7](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0b7)

Bump to pre-release 3.0.0b7
### Fixed
* [Typo in XRefPlanes #69](https://github.com/OCXStandard/OCX_Schema/issues/69)

### Changed
* [Move Area from Surface to Plate #87](https://github.com/OCXStandard/OCX_Schema/issues/87)
* [Change serialization of Vector3 #86](https://github.com/OCXStandard/OCX_Schema/issues/86)
* [Cardinalities of LimitedBy #79](https://github.com/OCXStandard/OCX_Schema/issues/79)
* [Naming duplicate between the OCX schema nad UnitsML schema: the Length type #78](https://github.com/OCXStandard/OCX_Schema/issues/78)

### Removed
* [#76 OcxItemPtr can be used in replacement for specific reference types](https://github.com/OCXStandard/OCX_Schema/issues/76)
* [Remove InnerContour from Plate #96](https://github.com/OCXStandard/OCX_Schema/issues/96)

### Added
*[Add a Generic Key Value Concept #12](https://github.com/OCXStandard/OCX_Schema/issues/12)

## [3.0.0b6] - 2024.01.09
Release tag [v3.0.0b6](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0b6)

Bump to pre-release 3.0.0b6

### Changed
1. [#72 Cardinality of elements and xs:choice](https://github.com/OCXStandard/OCX_Schema/issues/72)


## [3.0.0b5] - 2023.12.05

Bump to pre-release 3.0.0b5

### Removed
Release tag [v3.0.0b5](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0b5)

* [#73 Remove license boilerplate](https://github.com/OCXStandard/OCX_Schema/issues/73)

## [3.0.0b4] 2023.11.10
Release tag [v3.0.0b4](https://github.com/OCXStandard/OCX_Schema/releases/tag/v3.0.0b4)

Bump to pre-release 3.0.0b4



### Fixed
* [#70 Typo in Point3D](https://github.com/OCXStandard/OCX_Schema/issues/70)


## [3.0.0b3] - 2023.10.26

Bump to 3.0.0b3

### Fixed
* [#60 Minor schema fixes](https://github.com/OCXStandard/OCX_Schema/issues/60)
### Changed
* [#63 Cleanup CoordinateSystem](https://github.com/OCXStandard/OCX_Schema/issues/63)
* [#64 Cleanup FeatureCope](https://github.com/OCXStandard/OCX_Schema/issues/64)

## [3.0.0b2] - 2023.09.22

Bumped to pre-release 3.0.0b2

### Removed
 * [#56 Remove SectionRef from EndCutEnd](https://github.com/OCXStandard/OCX_Schema/issues/56)
 * [#58 Remove unused substitution groups](https://github.com/OCXStandard/OCX_Schema/issues/58)

## [3.0.0b0] - 2023.09.20
Bumped to pre-release 3.0.0b0
### Changed
* [#49 ReferencePlanes & FrameTable: Revert changes in Issue #36](https://github.com/OCXStandard/OCX_Schema/issues/49)
### Removed
* [#35 Remove the duplicate trace line definition on the Stiffener and Seam](https://github.com/OCXStandard/OCX_Schema/issues/35)
* [#50 Remove WebContour and FlangeContour from the schema](https://github.com/OCXStandard/OCX_Schema/issues/50)
### Changed
* [#51 LimitedBy BoundingBox: Use the contour start and end points instead](https://github.com/OCXStandard/OCX_Schema/issues/51)


## [3.0.0a2] - 2023.09.08

### Changed
* [#41 Make Length and Area mandatory on geometry entities](https://github.com/OCXStandard/OCX_Schema/issues/41)
* [#40 rename edgeReinforcement attribute](https://github.com/OCXStandard/OCX_Schema/issues/40)
* [#36 Resolve naming confusion of FrameTables](https://github.com/OCXStandard/OCX_Schema/issues/36)
* [#8 Root Point vs Trace Line Definition](https://github.com/OCXStandard/OCX_Schema/issues/8)
### Removed
* [#35 Remove the duplicate trace line definition on the Stiffener](https://github.com/OCXStandard/OCX_Schema/issues/35)


## [3.0.0a1] - 2023.08.28

### Fixed
* [#42 Fix bug in ```Hole2D```](https://github.com/OCXStandard/OCX_Schema/issues/42)
* [#38 Broken link in ```ShipDesignation```](https://github.com/OCXStandard/OCX_Schema/issues/38)
### Changed
* [#20 Compact representation of ```Point3D```](https://github.com/OCXStandard/OCX_Schema/issues/20)



## [3.0.0a0] - 2023.07.10

### Removed
  - Delete ``SchemaChange`` documentation as we have converted to this ``CHANGELOG.md``
  - Remove ``substitutionGroup`` from ``entityRefBase`` and ``BoundedRef``
### Fixed
1. [#3 Fix bug in ```CompartmentFace```](https://github.com/OCXStandard/OCX_Schema/issues/3)
2. [#4 Fix bug in ```CompartmentFace```](https://github.com/OCXStandard/OCX_Schema/pull/4)
3. [#16 and #17 Fix schema typos](https://github.com/OCXStandard/OCX_Schema/issues/16)

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
1. [#2 Add public license to schema](https://github.com/OCXStandard/OCX_Schema/pull/2)
2. [#5 Assign a valid schema URL](https://github.com/OCXStandard/OCX_Schema/issues/5)
  - Add ``Hole2DContour`` to ``refType``
  - Include boilerplate Apache 2.0 license information to the ``Header`` attribute: ``license``.  (oca)  
### Changed
1. [#7 Bulb profile definition](https://github.com/OCXStandard/OCX_Schema/issues/7)
2. [#20 Add compact representation of points](https://github.com/OCXStandard/OCX_Schema/issues/20)
  - Made ``FlangeWidth`` optional on ``BulbFlat`` element.  (oca) ([#7](https://github.com/OCXStandard/OCX_Schema/issues/7))

## [2.8.6_fix] - 2022-10-06 
Intermediate version.

Release tag: [v2.8.6_fix](https://github.com/OCXStandard/OCX_Schema/releases/tag/v2.8.6_fix)


### Changed
  - Added the ``UnboundedGeometry`` tag to ``CompartmentFace``.  (oca)  ([#3](https://github.com/OCXStandard/OCX_Schema/issues/3))
## [2.8.6] - 2021-06-10
Bumped to version v2.8.6
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
  - Rename ``EdgeReinforcement -> FlangeEdgeReinforcement`` as we now introduced a new ``EdgeReinforcement`` concept.  (oca)  ``BracketParameters``

### Fixed
  - Make ``LimitedBy`` optional.  (oca)  ``Bracket``
  - Typo in the attribute name ``firstGridNumber``.  (oca)  ``XSpacingGroup``
  - Make ``LimitedBy`` optional.  (oca)  ``Pillar``
  - The ``FrameTables`` entity is kept for backward compatibility. It might change in a future schema version.  (oca)  ``CoordinateSystem``
  - Make attribute ``id`` mandatory on all elements inheriting from ``IdBase``.  (oca)  ``IdBase``
