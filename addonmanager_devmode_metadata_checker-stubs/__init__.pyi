import Addon
import FreeCAD as FreeCAD
import NetworkManager as NetworkManager
import addonmanager_metadata
import typing

class MetadataValidators:
    def validate_all(self, repos):
        """Developer tool: check all repos for validity and print report"""
    def validate_package_xml(self, addon: Addon.Addon):
        """Check the package.xml file for the specified Addon"""
    def validate_content(self, addon: Addon.Addon) -> typing.List:
        """Validate the Content items for this Addon"""
    def validate_top_level(self, addon: Addon.Addon) -> typing.List:
        """Check for the presence of the required top-level elements"""
    @staticmethod
    def validate_urls(urls) -> typing.List:
        """Check the URLs provided by the addon"""
    @staticmethod
    def validate_workbench_metadata(workbench: addonmanager_metadata.Metadata) -> typing.List:
        """Validate the required element(s) for a workbench"""
    @staticmethod
    def validate_preference_pack_metadata(pack: addonmanager_metadata.Metadata) -> typing.List:
        """Validate the required element(s) for a preference pack"""
