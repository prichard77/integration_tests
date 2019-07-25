# -*- coding: utf-8 -*-
"""Manual tests"""
import pytest

from cfme import test_requirements


@pytest.mark.manual
@test_requirements.discovery
@pytest.mark.tier(1)
def test_infrastructure_providers_rhevm_edit_provider_no_default_port():
    """
    Polarion:
        assignee: pvala
        casecomponent: Infra
        caseimportance: medium
        caseposneg: negative
        initialEstimate: 1/12h
        setup:
            1. Navigate to Compute > Infrastructure > Providers.
            2. Click on `Configuration` and select `Add a new Infrastructure provider`.
            3. Add a rhevm provider.
            4. Edit it and try to change it to another rhevm provider.
        testSteps:
            1. There shouldn't be any default API port.
        expectedResults:
            1. API port should be blank.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(1)
@test_requirements.discovery
def test_add_infra_provider_screen():
    """
    Polarion:
        assignee: pvala
        casecomponent: Infra
        caseimportance: medium
        initialEstimate: 1/2h
        setup:
            1. Navigate to Compute > Infrastructure > Providers.
            2. Click on `Configuration` and select `Add a new Infrastructure provider`.
        testSteps:
            1. test form validation using incorrect format for each field
            2. test wrong ip
            3. test wrong credentials
            4. test wrong security protocol
            5. test wrong provider type
        expectedResults:
            1. Form must not be validated.
            2. Form must not be validated.
            3. Form must not be validated.
            4. Form must not be validated.
            5. Form must not be validated.
    """
    pass


@test_requirements.general_ui
@pytest.mark.manual
@pytest.mark.tier(1)
@pytest.mark.meta(coverage=[1532404])
def test_provider_summary_topology():
    """
    Polarion:
        assignee: pvala
        casecomponent: Infra
        caseimportance: high
        initialEstimate: 1/2h
        setup:
            1. Add an infra provider.
        testSteps:
            1. Navigate to provider's summary page.
            2. Click on topology.
        expectedResults:
            1.
            2. Provider Topology must be displayed.

    Bugzilla:
        1532404
    """
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_setting_default_filter():
    """
    Verify the creation and proper functionality of default filters.

    Polarion:
        assignee: prichard
        casecomponent: Cloud
        caseimportance: low
        initialEstimate: 1/8h
        testSteps:
            1. Navigate to the Compute > Infrastructure > Hosts view.
            2. Select a filter that does not have "(Default)" appended to the name. Note items displayed.
            3. Click "Select Default" button.
            4. Logout and log back in to CloudForms and navigate back to the Hosts view.
        expectedResults:
            1. Hosts view is displayed with hosts filtered via the Default filter (denoted by
            "(Default)" next to the filter name in the dropdown).
            2. Items displayed in the hosts panel will be filtered based upon the filter selected.
            3. "(Default)" will be displayed beside the filter name in the dropdown.
            4. Hosts view will be displayed filtered via the new Default filter.
    """
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_properties():
    """
    Verify host comparisons view functionality
    I am breaking down tests into the compare sections
	properties, security, configuration, My company tags
	make sure to include attributes, mode,views and download.

    Polarion:
        assignee: prichard
        casecomponent: Cloud
        caseimportance: low
        initialEstimate: 1/8h
        testSteps:
            1. Navigate to the Compute > Infrastructure > Hosts view.
            2. Select at least 2 hosts by checking the box in upper left of host icons.
            3. Click "Compare Selected Items" under the "Configuration" dropdown.
            4. Click on "Host Properties(X)" in the Compare Host view.
            5. Click on "Host Properties(X)" again, in the Compare Host view.
            6. Click to expand the "Properties" comparison section, select "Hardware", and click "Apply".
            7. Click on "Hardware(X)" in the Compare Host view.
            8. Click on "Hardware(X)" again, in the Compare Host view.
            9. Click to expand the "Properties" comparison section, select "Network Adapters", and click "Apply".
            10. Click on "Network Adapters(X)" in the Compare Host view.
            11. Click on the "#X" items that apply to the network adaters.
            12. Click on the "#X" items again that apply to the network adaters.
            13. Click on "Network Adapters(X)" again, in the Compare Host view.
            **now uncheck Host properties and then Hardware in Comp sctions
        expectedResults:
            1. Hosts view is displayed with hosts filtered via the Default filter (denoted by
            "(Default)" next to the filter name in the dropdown).
            2. The selected hosts should be displayed with a blue border and checked checkbox.
            3. The "Compare Host / Node" view should be displayed.
            - icons are displayed for all and only selected hosts with hostname displayed
            - one of the host icons has the host denoted as "(base)" in the hostname
            - host properties row is displayed (default)
            - "% Matched" text or graphs are displayed
            - when 3 or more hosts are displayed, remove icons exist for all non-base hosts.
            4. The row should be expanded to display all of the properties compared. Items that do not match the base
            host should be in blue. There should be X properties displayed. Properties for non-base hosts should be in
            purple/dark blue.
            5. The Host properties should collapse to one row again.
            6. A hardware row should be added to the view for all hosts with % matching graphs displayed for non-base
            hosts.
            7. The row should be expanded and displayed with same requirements as in step 4.
            8. The hardware metrics should collapse to one row again.
            9. A network adapters row should be added to the view for all hosts with % matching graphs displayed for non-base hosts.
            10. The row should be expanded and displayed with same requirements as in step 4.
            11. The "#X" individual network adapter rows should be expanded and displayed with same requirements as in step 4.
            12. The Hardware metrics should collapse to one row again.

            ****add a step for clicking on the Properties checkbox to check all subsections.
    """
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_security():
    '''
    This is going to be the same test as test_host_comparison_properties, but for the Security Section.
    Make sure to expand all subsections and verify the correct display functionality.
    I will add some steps that reference the properties test.
    '''
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_configuration():
    '''
    This is going to be the same test as test_host_comparison_properties, but for the Configuration Section.
    Make sure to expand all subsections and verify the correct display functionality.
    I will add some steps that reference the properties test.
    '''
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_my_company_tags():
    '''
    This is going to be the same test as test_host_comparison_properties, but for the My Company Tags Section.
    Make sure to expand all subsections and verify the correct display functionality.
    I will add some steps that reference the properties test.
    '''
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_remove_hosts():
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_exists_mode():
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_compressed_view():
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_download():
'''
	include txt, csv, pdf-export + print
'''
    pass

@pytest.mark.manual
@test_requirements.infra_hosts
def test_host_comparison_multipleviews_interactions():
    pass