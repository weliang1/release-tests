import unittest
from oar.core.advisory_mgr import AdvisoryManager
from oar.core.advisory_mgr import Advisory
from oar.core.config_store import ConfigStore


class TestAdvisoryManager(unittest.TestCase):
    def setUp(self):
        self.am = AdvisoryManager(ConfigStore("4.12.11"))

    def test_init(self):
        pass

    def test_get_jira_issues(self):
        jira_issues = self.am.get_jira_issues()
        self.assertIn("OCPBUGS-10973", jira_issues)
        self.assertIn("OCPBUGS-10225", jira_issues)

    @unittest.skip("disable this case, will not update released advisory")
    def test_change_qe_owner(self):
        self.am.change_ad_owners()
        for ad in self.am.get_advisories():
            self.assertEqual(ad.get_qe_email(), "xx@redhat.com")

    def test_check_greenwave_cvp_test(self):
        abnormal_tests = self.am.check_greenwave_cvp_tests()
        self.assertTrue(len(abnormal_tests) == 0)

    def test_push_to_cdn(self):
        self.am.push_to_cdn_staging()

    @unittest.skip("disable this case by default")
    def test_change_ad_status(self):
        self.am.change_advisory_status("REL_PREP")

    @unittest.skip("disable this case by default")
    def test_drop_bugs(self):
        self.am.drop_bugs()

    def test_check_cve_tracker_bug(self):
        tracker_bugs = self.am.check_cve_tracker_bug()
        self.assertFalse(tracker_bugs)

    @unittest.skip("disable this case by default")
    def test_get_doc_security_approved_ads(self):
        doc_appr, prodsec_appr = self.am.get_doc_security_approved_ads()
        self.assertTrue(len(doc_appr) == 2)
        self.assertTrue(len(prodsec_appr) == 0)
