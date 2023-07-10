# OCX_Schema Changelog - Pre release changes (pre 2.8.6)
This  pre-release changelog is kept for historic reasons,
## 2.8.5 - 2020-03-16

  - Changed the isReversed xs:type from string to boolean on XRefPlanes.  (oca)  ``XRefPlanes``
  - Added a root point Origin and two direction vectors (UDirection, VDirection) to the BracketParameters to remove ambiguities in the mapping of penetration and end configuration types.  (oca)  ``BracketParameters``
  - Made LimitedBy on Plate a mandatory item as we need this information to correctly map plate limits.  (oca)  ``Plate``
  - Introduced a ChoiceOf either TraceLine or Curve3D type for Stiffener due to backward compatibility with old model unit test for Nauticus import. This will not impact existing exports for vendors.  (oca)  ``Stiffener``
  - Introduced a ChoiceOf either TraceLine or Curve3D type for Seam due to backward compatibility with old model unit test for Nauticus import. This will not impact existing exports for vendors.  (oca)  ``Seam``
  - Cleaned up the types inheriting from EntityRefBase and BoundedRef. Reference types referring an object without geometry shall inherit from EntityRefBase while reference types referring to objects with geometry shall inherit from BoundedRef.  (oca)  ``EntityRefBase``
  - Introduced a new abstract reference type BoundedRef where an optional BoundingBox element has been introduced. The BoundingBox will limit the extent of the referenced object geometry. This can help to resolve ambiguous LimitedBy definitions.  (oca)  ``BoundedRef``
  - Added the possibility to define an extruded surface by a base curve and a sweep direction and extent.  (oca)  ``ExtrudedSurface``
  - Changed NumberOfDecksAbove from a global element to an attribute on PrincipalParticulars.  (oca)  ``PrincipalParticulars``
  - Removed unused property type "scope" on NURBSproperties.  (oca)  ``NURBSproperties``
  - Added the possibility to assign a main frame attribute isMainSystem=true when multiple systems are defined. If only one system is defined, it is assumed that the exported system is the main system.  (oca)  ``FrameTables``
  - Added the possibility to specify an offset of FR0 from AP for the X frame positions. If not given, it is assumed that Fr0 is positioned at AP.  (oca)  ``XRefPlanes``
  - Annotated enumeration values for compartmentPurpose   (oca)  ``compartmentPurpose``
  - Annotated enumeration values for bulkCargoType  (oca)  ``bulkCargoType``
  - Annotated enumeration values for gaseousCargoType  (oca)  ``gaseousCargoType``
  - Annotated enumeration values for liquidCargoType  (oca)  ``liquidCargoType``
  - Annotated enumeration values for unitCargoType.  (oca)  ``unitCargoType``
  - Annotated enumeration values for bracket position.  (oca)  ``position``
  - Annotated enumeration values for freeboardType according to SOLAS LL 66.  (oca)  ``freeboardType``
  - Redefined material grade for normal and high strength steel in accordance with IACS UR W11.  (oca)  ``grade``
  - Deleted RefPlaneGroup from RefPlanes definition as we require the exporting application to export every frame instance with a unique GUID  (oca)  ``FrameTables``
  - Deleted Cyl_Group from the CylindricalAxes definition as we require the exporting application to export every frame instance with a unique GUID  (oca)  ``CylindricalAxes``
  - Changed the externalRefAttributes enumeration of ExternalGeometryRef to refer to the specific geometry file type (.stp, .igs and .jt)  (oca)  ``externalRefAttributes``
## 2.8.4 - 2020-01-13

  - Introduced a new attribute edgeReinforcementType on BracketParameters describing the different bracket reinforcement types.  (oca)  ``BracketParameters``
  - Added a new sub-element EdgeReinforcement to BracketParameters.  (oca)  ``BracketParameters``
  - Introduced a new sub-element EdgeReinforcement containing additional parameters for reinforced brackets.  (oca)  ``EdgeReinforcement``
  - Made SpeedFactor a Quantity_T type (carries a unit).  (oca)  ``SpeedFactor``
  - Made Cyl_Group a global element.  (oca)  ``Cyl_Group``
  - Made SectionOuterShape a global element.  (oca)  ``SectionOuterShape``
  - Made SectionInnerShape a global element.  (oca)  ``SectionInnerShape``
  - Made FlangeContour a global element.  (oca)  ``FlangeContour``
  - Made WebContour a global element.  (oca)  ``WebContour``
  - Made ChildRef a global element.  (oca)  ``ChildRef``
  - Made ExternalGeometryRef a global element.  (oca)  ``ExternalGeometryRef``
  - Made ApplicationRef a global element.  (oca)  ``ApplicationRef``
  - Made Reference a global element.  (oca)  ``Reference``
  - Corrected bug in ExternalGeometryRef (wrong implementation of super-type).  (oca)  ``ExternalGeometryRef``
  - Added missing StiffenedBy to Bracket.  (oca)  ``Bracket``
  - Bug in ApplicationRef, wrong implementation of mandatory attribute externalRef.  (oca)  ``ApplicationRef``
  - Deleted EndCutCatalogue.  (oca)  ``ClassCatalogue``
## 2.8.3 - 2019-11-11

  - ComposedOf is made optional on Panel. A Panel with no ComposedOf element is treated as a "virtual" Panel and is only used to limit other objects. It will not be in scope for verification.  (oca)  ``Panel``
  - Revised EntityRefBase_T so that the OCX export is valid using either a localRef or a GUIDRef, or both. But at least one must be present. This requires validation by XSD Version 1.1  (oca)  ``EntityRefBase_T``
  - Added OccurrenceGroup to the itemRef enumerator. RootRef can now also reference an OccurrenceGroup which means that the root node can be a folder.  (oca)  ``RootRef``
  - The Occurrence is now defined as an OcxItemPtr and is a direct reference to a part in the DesignView.  (oca)  ``DesignView``
  - Deleted ProductView from ocxXML to reside directly under the Vessel item.  (oca)  ``ocxXML``
  - Moved ProductView from ocxXML to reside directly under the Vessel item.  (oca)  ``Vessel``
  - Removed enum bracketType from BracketParameters. The Bracket has its own values in the functionType enumerator which shall be used to set the type. This is now the same pattern for Panel, Stiffener, Plate and Bracket.  (oca)  ``BracketParameters``
  - Extended the functionType with BRACKET types. This makes it more consistent as we will only have one source for function types in the schema.  (oca)  ``functionType``
  - Made Bracket a subtype of Plate. The Bracket elements inherit all Plate elements and extends the Plate with one additional element BracketParameters  (oca)  ``Bracket``
  - Added GasTight value to tightness enumerator. WaterTight will always be GasTight, but GasTight does not mean WaterTight.  (oca)  ``tightness``
  - Renamed enum value RefPlane to GridRef in the enumerator refType.  (oca)  ``refType``
  - Added the WebNoseHeight to the EndCut_T type.  (oca)  ``EndCut_T``
  - Added the FlangeNoseHeight to the EndCut_T type.   (oca)  ``EndCut_T``
  - Added an explicit TraceLine element under Pillar representing the Pillar trace curve in space as a Curve3D type. This improves the readability of the schema  (oca)  ``Pillar``
  - Added an explicit TraceLine element under Seam representing the landing curve (Curve3D) of the Seam on the parent surface. This improves the readability of the schema  (oca)  ``Seam``
  - Made PhysicalProperty mandatory for all elements inheriting from StructurePart.  (oca)  ``StructurePart_T``
  - Renamed TopologyItem_T to StructurePart_T as this is a more meaningful description of the element.  (oca)  ``StructurePart_T``
  - Renamed TopologyItem_T to StructurePart_T as this is a more meaningful description of the element.  (oca)  ``StructurePart_T``
  - Deleted the DetailedFlangeContour under Stiffener as it is duplicated by the FlangeContour element.  (oca)  ``Stiffener``
  - Deleted the DetailedWebContour under Stiffener as it is duplicated by the WebContour element.  (oca)  ``Stiffener``
  - Added an explicit TraceLine element under Stiffener representing the landing curve (Curve3D) of the stiffener on the parent surface. This improves the readability of the schema  (oca)  ``Stiffener``
## 2.8.2 - 2019-10-10

  - Changed name Origin to Center on the parametric Circle3D definition for clarity.  (oca)  ``Circle3D``
  - Moved WebContour and FlangeContour from EndCut to Stiffener as the contour returns the full stiffener contour with end-cuts at both ends.  (oca)  ``Stiffener``
  - Expanded the structure functionType with more types.  (oca)  ``functionType``
  - The reference to the connected/penetrated Plate/Pillar/Stiffener is made mandatory.  (oca)  ``ConnectionConfiguration_T``
  - The configuration type is made optional on the ConnectionConfiguration_T. If the configuration type is not specified, the stiffener either penetrates/connects a single Plate/Pillar/Stiffener object with no additional parameters given. The connected Plate/Pillar/Stiffener must be referenced.  (oca)  ``ConnectionConfiguration_T``
  - Defined KnotVector_T base type for KnotVector, UknotVector and VknotVector.  (oca)  ``KnotVector_T``
## 2.8.1 - 2019-07-03

  - Changed NeutralAxisU and NeutralAxisV from Quantity_T to Vector3D_T type.  (oca)  ``UserDefinedBarSection``
  - Added GaseousCargo according to ISO 10303-215:2004  (oca)  ``GaseousCargo``
  - Added UnitCargo according to ISO 10303-215:2004  (oca)  ``UnitCargo``
  - Added LiquidCargo according to ISO 10303-215:2004  (oca)  ``LiquidCargo``
  - Added BulkCargo according to ISO 10303-215:2004  (oca)  ``BulkCargo``
  - Made it voluntary to export either Compartment and PhysicalSpace or both on the Arrangement  (oca)  ``Arrangement``
  - Deleted ApplicationRef from Arrangement as this is duplication for information  (oca)  ``Arrangement``
  - Changed base to for Cell from EntityRefBase_T to EntityBase_T.  (oca)  ``Cell``
  - Added EndCut as a Catalogue item to describe the stiffener end features.  (oca)  ``EndCut``
  - Added EndCutEnd1 and EndCutEnd2 to Stiffener  representing stiffener features.  (oca)  ``Stiffener``
  - Reintroduced GUIDRef on BarSection as this broke the export when removed.  (oca)  ``BarSection``
  - Reintroduced GUIDRef on Material as this broke the export when removed.  (oca)  ``Material``
## 2.8.0 - 2019-05-13

  - Renamed Slot to SlotParameters  (oca)  ``SlotParameters``
  - The end cut parameters are made optional but must carry the mandatory sniped attribute  (oca)  ``EndCut_T``
  - Moved the EndCut parameters to the Stiffener physical object. A stiffener can now have end cut parameters at each end: EndCutAtEnd1 and EndCutAtEnd2  (oca)  ``Stiffener``
  - Redesigned the ConnectionConfiguration to include only references to the it's connected parts (Bracket, Stiffener).  (oca)  ``ConnectionConfiguration``
  - Moved BracketParameters from ConnectionConfiguration to the physical type Bracket.  (oca)  ``Bracket``
  - Removed BracketRef from BracketParameters .  (oca)  ``BracketParameters``
  - Removed mandatory GUID from Material catalogue item.  (oca)  ``Material``
  - Removed mandatory GUID from BarSection catalogue item.  (oca)  ``BarSection``
## 2.7.8 - 2019-05-06

  - Added new reference ExternalGeometryRef as optional element for all structure parts inheriting from StructureItem.  (oca)  ``StructurePart``
  - Added new reference ExternalGeometryRef for external geometry representations.  (oca)  ``ExternalGeometryRef``
  - Corrected: Arrangement now inherits from DescriptionBase_T instead of ExternalBase_T (which is deleted as superfluous).  (oca)  ``Arrangement``
  - Reordered the Surface and SurfaceCollection on the ReferenceSurfaces definition. ReferenceSurfaces may contain any number of Surface and SurfaceCollection objects in an arbitrary order  (oca)  ``ReferenceSurfaces``
  - Added slotType attribute to the Slot object to distinguish between Slit and Open slots.  (oca)  ``SlotParameters``
  - Renamed WeldLegLength to ConnectionLength on the Slot entity. This is in alignment with the definition in the DNV GL Rules and avoids any confusion with welding requirements.  (oca)  ``SlotParameters``
  - Renamed HoleShapes to HoleShapeCatalogue  (oca)  ``HoleShapeCatalogue``
  - Fixed typo on Slot parameter asymmetric  (oca)  ``SlotParameters``
## 2.7.7 - 2019-04-05

  - Fixed bug in the inheritance of FarBracket (corrected to BracketParameters_T)  (oca)  ``FarBracket``
## 2.7.6 - 2019-03-25

  - Added DistanceAbove and WeldLegLength to LugPlateRef.  (oca)  ``LugPlateRef``
  - Made GUIDRef attribute  optional on Hole2D catalogue items  (oca)  ``Hole2D``
  - Made BracketParameters attribute "position" optional with default value position=NearSide  (oca)  ``BracketParameters``
  - Moved the BracketRef pointer to be part of the FarBracket type to uniquely identify the FarBracket material and thickness.  (oca)  ``FarBracket``
  - Moved the BracketRef pointer to be part of the NearBracket type to uniquely identify the NearBracket material and thickness.  (oca)  ``NearBracket``
## 2.7.5 - 2019-02-22

  - Added type SurfaceCollection to ReferenceSurfaces.  (oca)  ``ReferenceSurfaces``
  - Created a new type SurfaceCollection which can contain any number of surfaces and be referenced by GUID or localRef.  (oca)  ``SurfaceCollection``
  - Moved BracketRef from DoubleBracket type to BracketParameters_T type definition.  (oca)  ``BracketParameters_T``
  - Moved DistanceAbove and DistanceBelow to LugPlateRef_T type definition.  (oca)  ``LugPlateRef_T``
  - Moved reference elements (BracketRef, PlateRef, PillarRef) to the ConnectionConfiguration_T type definition.  (oca)  ``ConnectionConfiguration_T``
  - Moved reference elements (BracketRef, PlateRef, PillarRef) to the Penetration_T type definition.  (oca)  ``Penetration_T``
  - Changed DryCargoDensity to global type Density on DryCargoProperties .  (oca)  ``DryCargoProperties``
  - Changed LiquidCargoDensity to global type Density on LiquidCargoProperties .  (oca)  ``LiquidCargoProperties``
  - Changed PillarMaterial to generic type MaterialRef for pillar type .  (oca)  ``Pillar``
  - Changed element name from Height to Diameter .  (oca)  ``Tube``
## 2.7.4 - 2019-02-04

  - Added an optional CopeLength to the FeatureCope.  (oca)  ``FeatureCope``
  - Added ReferenceSurfaces to Vessel to collect frequently used surfaces.  (bb)  ``ReferenceSurfaces``
  - Added a bracketType enumerator to BracketParameters.  (oca)  ``BracketParameters``
  - Removed Clearance from WebStiffenerWithDoubleBracket.  (oca)  ``WebStiffenerWithDoubleBracket``
  - Removed Clearance from WebStiffenerWithSingleBracket.  (oca)  ``WebStiffenerWithSingleBracket``
  - Added SoftToe details to BracketParameters.  (oca)  ``BracketParameters``
  - Deleted Clearance from the BracketParameters.  (oca)  ``BracketParameters``
  - Added structureFunction as optional attribute to Stiffener.  (oca)  ``Stiffener``
  - Added structureFunction as optional attribute to Plate.  (oca)  ``Plate``
## 2.7.3 - 2019-01-04

  - Moved the FaceBoundaryCurve definition from UnboundedGeometry back to Surface as agreed in the progress meeting.  (oca)  ``Surface``
## 2.7.2 - 2019-01-03

  - Introduced a CompartmentFace entity as a specialisation of UnboundedGeometry where the FaceBoundaryCurve is made mandatory. Introduced a CompartmentFace entity as a specialisation of UnboundedGeometry where the FaceBoundaryCurve is made mandatory.   (oca)  ``CompartmentFace``
  - Moved the FaceBoundaryCurve definition from Surface to UnboundedGeometry (optional). This gives a clearer schema interpretation.  (oca)  ``Surface``
  - Moved the FaceBoundaryCurve definition from Surface back to UnboundedGeometry (optional). This gives a clearer schema interpretation.  (oca)  ``UnboundedGeometry``
  - Added Header element to Arrangement so that the original source can be traced with time stamp, author, system etc.  (oca)  ``Arrangement``
  - Added Compartment as sub-element to Arrangement. The compartment defines a closed volume consisting of FaceBoundary objects and do not depend on the presence of any structure Panels. This allows for the definition of compartments independent of any structure.  (oca)  ``Compartment``
  - Added Arrangement as a sub-element to Vessel. The Arrangement defines the vessel capacity plan composed of compartments  (oca)  ``Arrangement``
  - Renamed Compartment to PhysicalSpace to distinguish this definition of spaces which is defined by limits of physical structure Panel objects.  (oca)  ``PhysicalSpace``
## 2.7.1 - 2018-11-23

  - Made material Offset optional on the Plate  (oca)  ``Plate``
  - Modified the functionType enumerator to be aligned with AP218 coding and IACS Rec 82 glossary.  (oca)  ``functionType``
  - Added lug parameters to the LugPlateRef reference.  (oca)  ``LugPlateRef``
  - Added an optional SlotContour as part of the CutBy to give the full detail of the slot contour.  (oca)  ``CutBy``
## 2.7.0 - 2018-11-12

  - Changed the definition of the NURBSSurface to use the same nurbsAttributes as NURBS3D.  (oca)  ``NURBSSurface``
  - Changed the definition of the NURBS3D to reflect the NURBSSurface implementation (same structure).  (oca)  ``NURBS3D``
  - Changed the definition of the KnotVector to be a list of knot values and removed the multiplicity sub element.  (oca)  ``KnotVector``
  - Renamed bracketReinforcement to hasBracketReinforcement and changed type to boolean.  (oca)  ``hasBracketReinforcement``
  - Renamed Rectangular to RectangularHole for clarity.  (oca)  ``RectangularHole``
  - Changed the implementation of the nurbsAttributes on the NURBSSurface.  (oca)  ``NURBSSurface``
  - Changed the implementation of the NURBSParameters on NURBS3D curve to be aligned with the NURBS surface implementation.  (oca)  ``NURBS3D``
  - Changed the implementation of V_NURBSproperties to use the attribute group nurbsAttributes.  (oca)  ``V_NURBSproperties``
  - Changed the implementation of U_NURBSproperties to use the attribute group nurbsAttributes.  (oca)  ``U_NURBSproperties``
  - Changed the name of the attributeGroup nurbs3DAttributes  to nurbsAttributes  (oca)  ``nurbsAttributes``
  - Added Unose and Vnose to BracketParameters and removed Clearance.  (oca)  ``BracketParameters``
  - Added optional arbitrary Contour3D to a UserDefinedBarSection. Used for display purposes.  (oca)  ``UserDefinedBarSection``
  - Renamed UserDefined to UserDefinedBarSection which is a more self explained name.  (oca)  ``UserDefinedBarSection``
  - Renamed HoleShape to HoleShapes to reflect that this is a catalogue of many standard hole shapes.  (oca)  ``HoleShapes``
  - Replaced the generic Curve3D type by Contour3D on Hole2D to enforce a closed contour to describe arbitrary hole shapes.  (oca)  ``Hole2D``
  - Deleted Knots3D and added one UknotVector and one VknotVector to NURBS3D  (oca)  ``NURBS3D``
  - Revised the definition of WebStiffenerWithDoubleBracket to reference the DoubleBracket type  (oca)  ``WebStiffenerWithDoubleBracket``
  - Revised the definition of WebStiffenerWithSingleBracket to reference the SingleBracket type  (oca)  ``WebStiffenerWithSingleBracket``
  - Deleted the AsymmetricalHole type.  (oca)  ``ParametricHole2D``
  - Renamed FeatureCope parameters to CopeHeight and CopeRadius.  (oca)  ``FeatureCope``
  - Made BarSection sub elements (the different bar section subtypes) global and referenced from the BarSection.  (oca)  ``BarSection``
  - Included u and v offsets on SectionRef to allow the correct positioning of a Stiffener. u and v offsets are given relative to the trace line.  (oca)  ``SectionRef``
## 2.6.3 - 2018-10-17

  - Reverted change on XSectionCatalogue made in the previous version of the schema.  (oca)  ``XSectionCatalogue``
  - Reverted changes on BarSection made in the previous version of the schema.  (oca)  ``BarSection``
## 2.6.2 - 2018-10-17

  - Made FreeEdgeCurve3D referable by inheriting from EntityBase.  (oca)  ``FreeEdgeCurve3D``
  - Made LimitedBy optional for Plate.  (oca)  ``Plate``
  - Made LimitedBy optional for Panel.  (oca)  ``Panel``
  - Made the BarSection type abstract. All section types must inherit from the BarSection and are made a global element. This allows to uniformly treat reading and writing of section types.  (oca)  ``BarSection``
## 2.6.1 - 2018-10-08

  - Removed the  ConfigurationRef (reference to other stiffener end configuration) from the Pillar to avoid circular dependency.  (oca)  ``Pillar``
  - Removed the  ConfigurationRef (reference to other stiffener end configuration) from the Stiffener to avoid circular dependency.  (oca)  ``Stiffener``
  - Changed CellConnection to reference exactly two cells using the CellRef type.  (oca)  ``CellConnection``
  - Changed CellRef to OcxItemPtr type.  (oca)  ``CellRef``
  - Changed HoleRef to OcxItemPtr type.  (oca)  ``HoleRef``
  - Changed CrossSection to SectionRef on the Pillar type.  (oca)  ``Pillar``
  - Changed cardinality of FreeEdgeCurve3D. A FreeEdgeCurve3D need to contain at least one Curve3D, and can be a combination of different unlimited Curve3D types in any sequence.  (oca)  ``FreeEdgeCurve3D``
  - Renamed DEXItemPtr to OcxItemPtr.  (oca)  ``OcxItemPtr``
  - Added enumerator for the bracket position.  (oca)  ``BracketParameters``
## 2.6.0 - 2018-09-30

  - Changed Schema name space from dex to ocx.  (oca)  ``ocxXML``
  - Made it possible to specify only one Inclination in case of a straight stiffener trace line.  (oca)  ``Stiffener``
  - Removed NurbsSurfaceCollection as this is an unnecessary layer.  (oca)  ``Surface``
  - Made FaceBoundaryCurve optional for all surfaces which inherit from Surface .  (oca)  ``Surface``
  - Made CellConnection a global element.  (oca)  ``CellConnection``
  - Added FreeEdgeCurve3D to the enumeration types.  (oca)  ``refType``
  - Changed from Member to Pillar in the enumeration types.  (oca)  ``refType``
  - A Stiffener may be attached to a Plate, a Pillar or another Stiffener at the configuration position.  (oca)  ``ConnectionConfiguration``
  - A Penetration can either penetrate a Plate, a Pillar or a Stiffener.  (oca)  ``Penetration``
## 2.5.3 - 2018-09-05

  - StiffenerRef attribute on the WebStiffenerWithDoubleBracket object is now explicitly made a DexItemPtr_T type.  (oca)  ``WebStiffenerWithDoubleBracket``
  - StiffenerRef attribute on the WebStiffenerWithSingleBracket object is now explicitly made a DexItemPtr_T type.  (oca)  ``WebStiffenerWithSingleBracket``
  - StiffenerRef attribute on the WebStiffener object is now explicitly made a DexItemPtr_T type.  (oca)  ``WebStiffener``
  - BracketRef attribute on the WebStiffenerWithDoubleBracket object is now explicitly made a DexItemPtr_T type.  (oca)  ``WebStiffenerWithDoubleBracket``
  - BracketRef attribute on the WebStiffenerWithSingleBracket object is now explicitly made a DexItemPtr_T type.  (oca)  ``WebStiffenerWithSingleBracket``
  - BracketRef attribute on the DoubleBracket object is now explicitly made a DexItemPtr_T type.  (oca)  ``DoubleBracket``
  - CutBy element on the Stiffener object is now explicitly made a CutBy_T type.  (oca)  ``Stiffener``
  - Moved FaceBoundaryCurve from UnboundedGeometry to NURBSSurface_T definition  (oca)  ``NURBSSurface_T``
  - renamed attributes on  NurbsSurfaceProps_T to follow the naming convention.  (oca)  ``NurbsSurfaceProps_T``
## 2.5.2 - 2018-08-28

  - Made ConnectionConfiguration an element directly under Stiffener with cardinality [0,2]   (oca)  ``Stiffener``
  - Made ConnectionConfiguration an element directly under Pillar with cardinality [0,2]   (oca)  ``Pillar``
  - Replaced PillarCenterline with Curve3D  (oca)  ``Pillar``
  - Replaced StiffenerTraceLine with Curve3D  (oca)  ``Stiffener``
  - Made CrossSectionRef and MaterialRef  elements directly under Stiffener  (oca)  ``Stiffener``
  - Added an optional FaceBoundaryCurve to the UnboundedGeometry for panels/plates  (oca)  ``UnboundedGeometry``
  - Removed ComposedOf from Compartment and moved the Cell reference (one to many) to directly under Compartment.  (oca)  ``Compartment``
  - Added Pillar as part of ComposedOf for a Panel  (oca)  ``ComposedOf``
  - Added an optional LimitedBy to Plane3D to avoid having to intersect co-planar objects.  (oca)  ``Plane3D``
  - Introduced units for the Start and Spacing elements on RefPlaneGroup  (oca)  ``RefPlaneGroup``
  - Introduced units for the Offset on GridRef.  (oca)  ``GridRef``
  - Made localRef a mandatory attribute on EntityRefBase. All classes derived from EntityRefBase need to provide a localRef.  (oca)  ``EntityRefBase``
  - EntityRefBase no longer inherit from IdBase and DescriptionBase to compact the information to be outputted for references. All classes derived from EntityRefBase does not need to provide an id or a Description.  (oca)  ``EntityRefBase``
  - Removed BracketShape from the Catalogue as all brackets are defined in place.  (oca)  ``ClassCatalogue``
  - Renamed TrimCurves to OuterContour.  (oca)  ``Panel``
  - Renamed TrimCurves to OuterContour.  (oca)  ``Plate``
  - Added a second FeatureCope (FeatureCopeU and FeatureCopeV) to the BracketParameters type to support asymmetric bracket shapes.  (oca)  ``BracketParameters``
  - Renamed ManHoleSymmetrical to SymmetricalHole  (oca)  ``SymmetricalHole``
  - Renamed ManHoleAsymmetrical to AsymmetricalHole  (oca)  ``AsymmetricalHole``
  - Added a new parametric hole definition RectangularMickeyMouseEars.  (oca)  ``RectangularMickeyMouseEars``
  - Renamed simple element Grade to grade in accordance with the naming conventions.  (oca)  ``grade``
  - Renamed simple type Description_T to Description_T in accordance with the naming conventions.  (oca)  ``Description_T``
  - BuilderInformation_T element was incorrectly named BuilderInformation_T. Renamed the element to BuilderInformation in accordance with the naming conventions.  (oca)  ``BuilderInformation``
  - ClassCatalogue derives from DescriptionItem instead of Function (unnecessary layer of abstraction).  (oca)  ``ClassCatalogue``
  - Added InnerContour to CutBy to allow for any generic opening definition composed of a set of trim curves.   (oca)  ``CutBy``
  - Removed item references derived from DEXItemPtr to simplify the schema.  (oca)  ``DEXItemPtr``
  - Modified DEXItemPtr refType to include a list of allowed reference items.  (oca)  ``refType``
  - Fixed typo in naming of IntermediatePoint in CircumArc3D  (oca)  ``CircumArc3D``
## 2.5.1 - 2018-06-29

  - Deleted the StructureFunction element, and added structureFunction as an optional attribute to Plate  (oca)  ``Plate``
  - Deleted the StructureFunction element, and added structureFunction as an optional attribute to Stiffener  (oca)  ``Stiffener``
  - Deleted the StructureFunction element, and added structureFunction as a mandatory attribute to Panel  (oca)  ``Panel``
  - Made the tightness attribute mandatory on Panel.  (oca)  ``Panel``
  - Removed Instance attribute from Panel (The Instance attribute carried AsDefined, Reflected, Both). The schema will instantiate all parts.  (oca)  ``Panel``
  - Removed Knots2D from NURBS3D and replaced with the Knot element  (oca)  ``NURBS3D``
  - Added Bracket to Vessel at same level as Panel, Plate, Stiffener ....  (oca)  ``Vessel``
## 2.5.0 - 2018-06-28

  - Added position attribute to BracketParameters to specify Near or Far.  (oca)  ``BracketParameters``
  - Removed NurbsSurfacePatch from NURBSSurfaceCollection The NURBSSurfaceCollection contains a set of NurbsSurface definitions.  (oca)  ``NURBSSurfaceCollection``
  - Removed RangeBox3D as it is not used.  (oca)  ``GeometryRepresentation``
  -             The panel UnboundedGeometry can consist of multiple surfaces to enable the definition of knuckled panels.  (oca)  ``Panel``
  - A plate can have its own UnboundedGeometry.  (oca)  ``Plate``
  - Added a position (near/far) to the BracketParameters  (oca)  ``BracketParameters``
  - Added a cargo type to the Compartment definition to separate compartment and cargo physical properties.  (oca)  ``Compartment``
  - Removed PhysicalProperties from Seam.  (oca)  ``Seam``
  - Revised StructureFunction as agreed in distributed spreadsheet. Structure Functions are only one level, and the type is enumerated.  (oca)  ``StructureFunction``
  - Material side has been removed from the Plate element. The associated PrincipalVesselDirection is discontinued and has been deleted from the schema.The Offset uniquely defines the material offset from the mould line together with the surface normal.  (oca)  ``Plate``
  - Added OccurrenceGroup to the ProductView to support nested levels of grouping of instances.  (oca)  ``OccurrenceGroup``
  - Renamed AssemblyView to DesignView.  (oca)  ``DesignView``
## 2.4.1 - 2018-06-12

  - Changed Hole2DContour to include a reference to a catalogue Hole2D type.  (oca)  ``Hole2DContour``
  - Added HoleRef to reference hole catalogue definitions.  (oca)  ``HoleRef``
  - Deleted TertiaryAxis from the definition of the Transformation  (oca)  ``Transformation``
  - Changed UnboundedPanelGeometry to global element UnboundedGeometry for the Panel.  (oca)  ``Panel``
  - Added UnboundedGeometry to the Plate and Bracket definitions.  (oca)  ``Plate``
  - Added a EdgeRef to LimitedBy enabling to define a closed contour by the limiting objects.  (oca)  ``LimitedBy``
  - Added a Cone3D surface type.  (oca)  ``Cone3D``
  - Renamed LineString3D to PolyLine3D. Deleted LineString3D as these represent the same line type  (oca)  ``PolyLine3D``
  - Deleted all Curve2D objects, and introduced a boolean is2D (default = false) on Curve3D to allow restriction to 2D (Z coordinate can be assumed equal zero).  (oca)  ``Curve3D``
  - Stiffener/member inclination given by two direction vectors, one at each end.  (oca)  ``Inclination``
## 2.4.0 - 2018-06-12

  - Added an AssemblyView as a specialization of a ProductView.  (oca)  ``AssemblyView``
  - Added a generic ProductView to the schema. ProductView is abstract and is not instantiated.  (oca)  ``ProductView``
  - Changed Contour3D_T to explicitly distinguish between closed and open Curve3D types.  (oca)  ``Contour3D_T``
  - Added PolyLine3D to the set of Curve3D types definition to Ellipse3D.  (oca)  ``PolyLine3D``
  - Added MinorAxis definition to Ellipse3D.  (oca)  ``Ellipse3D``
  - Made LimitedBy to a common global element and included the possibility to reference any structure object as part of the topology.  (oca)  ``LimitedBy``
  - Added the possibility to reference Members and Plates from a ConnectionConfiguration.  (oca)  ``ConnectionConfiguration``
  - Added new pointer type MemberRef to reference instantiated members (Pillars).  (oca)  ``MemberRef``
  - Added a position (Point3D) to the Inclination definition of the Stiffener. It is required to specify the inclination at both stiffener ends and at intermediate positions if necessary.  (oca)  ``Stiffener``
  - Cleaned up the CoordinateSystem definitions and naming of elements and attributes.  (oca)  ``CoordinateSystem``
  - Grouped all RefPlanes under a FrameTable element in CoordinateSystem to improve schema readability.  (oca)  ``CoordinateSystem``
  - Changed Vector2D to be unit less and of unit length  (oca)  ``Vector2D``
  - Changed Vector3D to be unit less and of unit length  (oca)  ``Vector3D``
  - Added Compartment definition to the schema. A Compartment represents a physical volume.  (oca)  ``Compartment``
  - Added Designation information to the Vessel.  (oca)  ``ShipDesignation_T``
## 2.3.2 - 2018-05-28

  - Allow for instantiation of any structure object directly under the Vessel.  (oca)  ``Vessel``
  - Added a Penetration object to  pillars.  (oca)  ``Pillar``
  - Added the possibility for a Stiffener to penetrate another stiffener by modification of the Penetration object.  (oca)  ``Penetration``
  - Added CutBy element to the Pillar to allow for the definition of arbitrary openings in members  (oca)  ``Pillar``
  - Added CutBy element to the Stiffener to allow for the definition of arbitrary openings in stiffeners.  (oca)  ``Stiffener``
  - Changed Inclination definition of Pillar to be the same as the definition for Stiffener.  (oca)  ``Pillar``
  - Corrected name of PhysicalProperties_Type to PhysicalProperties_T to align with naming convention.  (oca)  ``PhysicalProperties``
  - Corrected typo of IntermediatePoint in CircumArc2D.  (oca)  ``CircumArc2D``
## 2.3.1 - 2018-05-15

  - Added a direction vector for the stiffener flange to define the local orientation of the Stiffener cross-section.  (oca)  ``Stiffener``
  - Added additional metadata to BarSection.  (oca)  ``BarSection``
  - Changed BulbFlat properties to include bulb width.  (oca)  ``BulbFlat``
  - Changed Segment definition of CompositeCurve3D to be the same definition as for CompositeCurve2D.  (oca)  ``CompositeCurve3D``
  - Changed Segment definition of CompositeCurve2D to unbounded. A Segment may either consist of one Line2D, one CircumArc2D or both types in combination.  (oca)  ``CompositeCurve2D``
## 2.3.0 - 2018-04-16

  - Added NURBSSurfaceCollection as a collection of NURBSSurfaces.  (oca)  ``NURBSSurfaceCollection``
  - Removed LineArc2D which is replaced by CircumArc2D.  (oca)  ``CircumArc2D``
  - Redefined CompositeCurve2D to a collection of Line2D and CircumArc2D types.  (oca)  ``CompositeCurve2D``
  - Added a straight line Line2D defined by two positions.  (oca)  ``Line2D``
  - Added PhysicalProperties information to Plate, Bracket, Stiffener and Member types.  (oca)  ``PhysicalProperties``
  - Added Pillar as a specialization of the Member type.  (oca)  ``Pillar``
  - Redefined CompositeCurve3D to a collection of Line3D and CircumArc3D types.  (oca)  ``CompositeCurve3D``
  - Added a straight line Line3D defined by two positions.  (oca)  ``Line3D``
  - Removed LineArc3D which is replaced by CircumArc3D.  (oca)  ``CircumArc3D``
  - Changed attribute naming in accordance with the lCC (lowerCamelCase) naming convention for attributes.  (oca)  ``bracketReinforcement``
  - Removed Transformation as part of the Bracket definition as each bracket will be directly instantiated in 3D space.  (oca)  ``Bracket``
  - Removed Centroid attribute from Surface objects to make the XML more compact.  (oca)  ``Surface``
  - Removed Centroid attribute from Curve3D objects to make the XML more compact.  (oca)  ``Curve3D``
  - Removed Centroid attribute from Curve2D objects to make the XML more compact.  (oca)  ``Curve2D``
  - Removed StructureGrouping and Structure containers from the schema. Panel or Plate objects are placed directly under the Vessel.  (oca)  ``Vessel``
  - Added two additional enumerations to the PrincipalVesselDirection: WithSurfaceNormal and AgainstSurfaceNormal.  (oca)  ``PrincipalVesselDirection``
  - Added unbounded geometry definition to Bracket.  (oca)  ``Bracket``
  - Changed trim curves of Bracket from 2DCurve to 3DCurve.  (oca)  ``Bracket``
  - Added a PlateRef as a specialization of the EntityRefBase.  (oca)  ``PlateRef``
## 2.2.0 - 2018-04-05

  - Added RangeBox3D as new geometry type defining a box shape by min and max extensions.  (oca)  ``GeometryRepresentation``
  - Added Sphere3D as new Surface type defining a sphere by radius and origin.  (oca)  ``Sphere3D``
  - Added CircumCircle3D as new Curve3D type defining a circum circle by 3 points.  (oca)  ``CircumCircle3D``
  - Added CircumArc3D as new Curve3D type defining a circular arc by 3 points.  (oca)  ``CircumArc3D``
  - Added Ellipse3D as new Curve3D type  (oca)  ``Ellipse3D``
  - Added Circle3D as new Curve3D type  (oca)  ``Circle3D``
  - Changed content in Knot_T from elements to attributes as these are parameters without unit (not of type Quantity). Makes the XML more compact.  (oca)  ``Knot_T``
  - Extended the number of characters to 40 for the GUIDRef to match guids in the Aveva export  (oca)  ``GUIDRef``
  - Made the ref  attribute optional for all elements inherited from EntityRefBase. This makes the schema more flexible, but it can also be rendered incomplete.To be discussed. Maybe we can have a mandatory choice between one of the two reference types: ref or GUIDRef.  (oca)  ``EntityRefBase``
  - Made the id  attribute optional for all elements inherited from IdBase. This makes the schema more flexible, but it can also be rendered incomplete.To be discussed.  (oca)  ``IdBase``
  - Added an AngleTolerance measure.   (oca)  ``Form``
  - Renamed the Tolerance measure to DistanceTolerance.   (oca)  ``Form``
  - Made the Tolerance measure provided by the exporting application global for all geometries by moving it to the Form type.   (oca)  ``Form``
  - Changed type of Centroid definition to Point3D on surfaces  (oca)  ``Surface``
  - Changed type of Centroid definition to Point3D on 3D curves  (oca)  ``Curve3D``
  - Changed type of Centroid definition to Point2D on 2D curves  (oca)  ``Curve2D``
## 2.1.0 - 2018-03-22

  - Added a complex curve CompositeCurve2D  (oca)  ``CompositeCurve2D``
  - Added a complex curve CompositeCurve3D  (oca)  ``CompositeCurve3D``
  - Made it possible for a stiffener to reference an ConnectionConfiguration where an existing ConnectionConfiguration points to me  (oca)  ``Stiffener``
  - Added bracket parameters BracketParameters  (oca)  ``BracketParameters``
  - Specialized a reference type ConfigurationRef  (oca)  ``ConfigurationRef``
  - Specialized a reference type BracketRef.  (oca)  ``BracketRef``
  - Specialized a reference type StiffenerRef.  (oca)  ``StiffenerRef``
  - Added a 3D position to an ConnectionConfiguration  (oca)  ``ConnectionConfiguration``
  - Added parameters for possible types of ConnectionConfiguration  (oca)  ``ConnectionConfiguration``
  - Added bracket and stiffener detailing FeatureCope.  (oca)  ``FeatureCope``
  - Made the GUIDRef optional for all elements derived from GeometryRepresentation.  (oca)  ``GeometryRepresentation``
## 2.0.0 - 2018-03-14

  - Added a specialized SectionRef pointer  (oca)  ``SectionRef``
  - Added parametric hole shape definitions to catalogue Hole2D   (oca)  ``Hole2D``
  - Added EntityRefBase item as a base class to all references.   (oca)  ``EntityRefBase``
  - Introduced DEXItemPtr as a general DEX pointer to any item derived from EntityBase.   (oca)  ``DEXItemPtr``
  - Renamed GridReference to GridRef which inherit from EntityRefBase.   (oca)  ``GridRef``
  - Included a unique ID on the Material_T type.   (oca)  ``Material``
  - PlateMaterial now inherit from EntityRefBase supporting the general reference mechanism in the schema.   (oca)  ``PlateMaterial``
  - Stiffener type uses new reference mechanism EntityRefBase to associate material and cross-section.  (oca)  ``Stiffener``
  - Added a Tolerance measure to all GeometryRepresentations.   (oca)  ``GeometryRepresentation``
  - Added Centroid and Area attributes to all surfaces.   (oca)  ``Surface``
  - Added Centroid and Length attributes to all curves   (oca)  ``Curve3D``
  - Changed to English writing style Catalog->Catalogue   (oca)  ``ClassCatalogue``
  - Either Structure or StructurGrouping can be sub-nodes to the Vessel type.The schema no longer require an instance of a StructureGrouping if this level is not necessary.   (oca)  ``Vessel``
  - Added TrimCurves to the Plate.   (oca)  ``Plate``
  - Added ClassificationData to the Vessel. ClassificationData now contains PrincipalParticulars and other class related data  (oca)  ``Vessel``
  - Renamed Entity_T with IdBase_T  (oca)  ``IdBase``
  - Added optional TonnageData to the Vessel definition   (oca)  ``ocx:TonnageData_T``
  - Added optional StatutoryData to the Vessel definition   (oca)  ``ocx:StatutoryData_T``
  - Added optional language attribute xs:language   (oca)  ``dexXML``
  - Replaced uos with DocumentBase and introduced a schemaVersion attribute  (oca)  ``DocumentBase``
