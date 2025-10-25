# banana_api/tests/test_treatments_api.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker

from banana_api.models import Disease, Treatment


class TreatmentApiTests(APITestCase):
    def setUp(self):
        # สร้างโรคไว้ผูกกับการรักษา
        self.d1, self.d2 = baker.make(Disease, _quantity=2)
        # d1 มี 3 วิธีรักษา, d2 มี 2 วิธีรักษา รวม 5 รายการ
        self.treatments_d1 = baker.make(Treatment, disease=self.d1, _quantity=3)
        self.treatments_d2 = baker.make(Treatment, disease=self.d2, _quantity=2)
        self.total = 5

    def _assert_disease_field(self, disease_field, expected):
        """
        รองรับทั้งแบบ pk (int) หรือ nested object (ถ้า serializer ทำ nested)
        """
        if isinstance(disease_field, int):
            self.assertEqual(disease_field, expected.pk)
        elif isinstance(disease_field, dict):
            self.assertIn("disease_id", disease_field)
            self.assertEqual(disease_field["disease_id"], expected.pk)
        else:
            self.fail(f"Unexpected disease field type: {type(disease_field)}")

    def test_list_treatments_default_pagination(self):
        """
        GET /api/treatments/ → 200
        default page=1, size=10
        """
        url = reverse("treatment_list")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        body = res.json()

        for key in ["count", "total_pages", "current_page", "page_size", "results"]:
            self.assertIn(key, body)

        self.assertEqual(body["count"], self.total)
        self.assertEqual(body["current_page"], 1)
        self.assertEqual(body["page_size"], 10)
        self.assertEqual(len(body["results"]), self.total)  # 5 < 10

        item = body["results"][0]
        for k in ["treatment_id", "method", "source", "disease"]:
            self.assertIn(k, item)

    def test_list_treatments_custom_page_and_size(self):
        """
        page=1,size=2 → 2 รายการ
        page=3,size=2 → 1 รายการ (รวม 5)
        """
        url = reverse("treatment_list")

        r1 = self.client.get(url, {"page": 1, "size": 2})
        self.assertEqual(r1.status_code, status.HTTP_200_OK)
        b1 = r1.json()
        self.assertEqual(b1["current_page"], 1)
        self.assertEqual(b1["page_size"], 2)
        self.assertEqual(len(b1["results"]), 2)
        self.assertEqual(b1["count"], self.total)
        self.assertEqual(b1["total_pages"], 3)

        r3 = self.client.get(url, {"page": 3, "size": 2})
        self.assertEqual(r3.status_code, status.HTTP_200_OK)
        b3 = r3.json()
        self.assertEqual(b3["current_page"], 3)
        self.assertEqual(b3["page_size"], 2)
        self.assertEqual(len(b3["results"]), 1)
        self.assertEqual(b3["count"], self.total)
        self.assertEqual(b3["total_pages"], 3)

    def test_list_treatments_invalid_query_params_return_400(self):
        """
        page/size ผิดรูปแบบ → 400
        """
        url = reverse("treatment_list")
        res = self.client.get(url, {"page": "abc", "size": "-5"})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_treatment_detail_ok(self):
        """
        GET /api/treatments/<pk>/ → 200
        primary key = treatment_id
        """
        obj = self.treatments_d1[0]
        url = reverse("treatment-detail", args=[obj.pk])  # obj.pk == treatment_id
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.json()

        for k in ["treatment_id", "method", "source", "disease"]:
            self.assertIn(k, data)
        self.assertEqual(data["treatment_id"], obj.treatment_id)
        self._assert_disease_field(data["disease"], obj.disease)

    def test_get_treatment_detail_404(self):
        url = reverse("treatment-detail", args=[999999])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
