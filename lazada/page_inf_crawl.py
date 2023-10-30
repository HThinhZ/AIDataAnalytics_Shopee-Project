import requests
import pandas as pd
import csv
import json
import re
import time
import random
import sys

cookie_lis = ['__wpkreporterwid_=ccffb3c9-d8b8-471b-0e25-afcd31056f8f; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; xlly_s=1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19656%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698812900%7C3%7CMCAAMB-1698812900%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698215300s%7CNONE%7CvVersion%7C5.2.0; _m_h5_tk=63ef50b11341dd3743be7128a17c3716_1698295693478; _m_h5_tk_enc=14cd7a129aaea84d096bda9ce10ca360; _ga_3V5EYPLJ14=GS1.2.1698292548.15.1.1698292548.60.0.0; epssw=1*TVls11GPo1dFtEz4uWsGt1ITHRg4u5b4NAMOZrsJiUFwuW1Ic733-5B5NKQ-d5B56T15k1jCblydLbJKdtRkFCB51TsGiDSeNZyG6hBfG47N6fvScIkqtJyT9ECCmQgRBdqKBk0c34LRT4pnx8B4etyR38pq_1WRn8B4yaBBLgp1jMPtT5bwh8HRnkmnxDq3xf..; t_sid=6uqBGDUkv8AsG0zMYYNhodAVeOrMeTcp; utm_channel=NA; isg=BFpa8A2V62-5QGaDtF16LfK_qwB8i95l4TCrpGTTBu241_oRTBsudSAhp7vLXlb9',
              '__wpkreporterwid_=310a2921-e0d5-431f-b10e-f547968277d7; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; xlly_s=1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19656%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698812900%7C3%7CMCAAMB-1698812900%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698215300s%7CNONE%7CvVersion%7C5.2.0; t_sid=shcx0lVEeYSYxqhYDABLPygmE9q8NebH; utm_channel=NA; _m_h5_tk=659b6c5d7c72609efa8564b4b8601383_1698334921311; _m_h5_tk_enc=bc8bb804cea1de235a4c47b5538f1611; EGG_SESS=S_Gs1wHo9OvRHCMp98md7I7UyuMbdi04ZhBTtir5lFH-UZISZEA96R4eDyxSo88I2U3r_4JakpVsxCm728PUBRi4Q8DUfT5y2Ebhu41QzeF171cuPnWzP9yEW5U3Co_MOppVZaEo2F_k44K07EbSWRb5dCfzEk3pSIJ2URxbJXE=; _gat_UA-30172376-1=1; _ga_3V5EYPLJ14=GS1.2.1698327368.18.1.1698329300.60.0.0; epssw=1*MFO611iaG5FOG_GSuW_SZ-FFHRGku5b86R6As6CXIAvso4f87ubLuODNtCv_jcfOFGxGFxNnO2pidtR_NqWVdtSiep62dt7ChKv466pmTrpA6OR9F1BRNKKQFp9V-8pHneLauSTZidrFO7MZsm04-BUVZvTT-HaH3Je8dL3y7kqnyaBR3zQJyC2Cevp8hD7RyaB_CnUa3A448tmbSXDFW4yBFDVbE-onWaQRyah.; isg=BF5e7DsDt7OWh-IXGEm2YdZjr_SgHyKZBdwv0Ajn4KGAK_8FcK04qOLNIy8nShqx',
              '__wpkreporterwid_=310a2921-e0d5-431f-b10e-f547968277d7; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; xlly_s=1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19656%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698812900%7C3%7CMCAAMB-1698812900%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698215300s%7CNONE%7CvVersion%7C5.2.0; t_sid=shcx0lVEeYSYxqhYDABLPygmE9q8NebH; utm_channel=NA; _m_h5_tk=659b6c5d7c72609efa8564b4b8601383_1698334921311; _m_h5_tk_enc=bc8bb804cea1de235a4c47b5538f1611; EGG_SESS=S_Gs1wHo9OvRHCMp98md7I7UyuMbdi04ZhBTtir5lFH-UZISZEA96R4eDyxSo88I2U3r_4JakpVsxCm728PUBRi4Q8DUfT5y2Ebhu41QzeF171cuPnWzP9yEW5U3Co_MOppVZaEo2F_k44K07EbSWRb5dCfzEk3pSIJ2URxbJXE=; _ga_3V5EYPLJ14=GS1.2.1698327368.18.1.1698329300.60.0.0; epssw=1*i_dO11iKb1nsGODMuWsGt9tItdbdNAkG6R60VVyq7PzLMaf89TULuZPC9e2__8GWH_9vFxZLE1506TsupEWV6TtzhQ9A6TOM6e9j66pmTyM56OR9FGxwjhjQFp9V1X0Xut8tbjjnwsopFbV41WGX-BEWZ4B9S7gH3rgbxDD6uLp4xDDR38BqxkBQevp8i3Knx4QRxDDBJuC7L9xbSDmD7wwBFv_zE-onxv9-xDc.; isg=BK-vcxTaFhz-IhNgkXJ3vg-4PsO5VAN2LJf-x8E8S54lEM8SySSTxq3GkhguMdvu',
              '__wpkreporterwid_=310a2921-e0d5-431f-b10e-f547968277d7; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; xlly_s=1; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19658%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698981507%7C3%7CMCAAMB-1698981507%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698383907s%7CNONE%7CvVersion%7C5.2.0; t_sid=gdwX3sawOPW0TWqZGplZKc11Wu0HLE9l; utm_channel=NA; _m_h5_tk=9c6578c86c0843e992afac2ba4bbd5f5_1698431521727; _m_h5_tk_enc=d87ddc0b1987289827d1904f2b9e72e2; epssw=1*GsN611g5ZfnGTO2MJSesIUUSZ7tIfA2MIA8a7zeOZkcYkO427zFQtQh-H1B5NKCESGxMNKC5kGpvpxJdLlWMdtJ5Hp62bh-GiApVNZyG6p-MruaN6fvSE_VaObkZ7OdIm_nnI-oaKpveeJ9-pE9CeDmnxDDBe8Kpexz5PKe4etyR3kmnxb2qy2WmG5hG7dH4dLgRyaQRyaC.; _gat_UA-30172376-1=1; _ga_3V5EYPLJ14=GS1.2.1698421801.21.1.1698421801.60.0.0; isg=BDY2XLMPT7ogMjqf8JEeef6rh2w4V3qRfaRXWKAfIpm049Z9COfKoZyV-6eP7nKp',
              '__wpkreporterwid_=310a2921-e0d5-431f-b10e-f547968277d7; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; xlly_s=1; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19658%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698981507%7C3%7CMCAAMB-1698981507%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698383907s%7CNONE%7CvVersion%7C5.2.0; t_sid=gdwX3sawOPW0TWqZGplZKc11Wu0HLE9l; utm_channel=NA; _m_h5_tk=9c6578c86c0843e992afac2ba4bbd5f5_1698431521727; _m_h5_tk_enc=d87ddc0b1987289827d1904f2b9e72e2; _ga_3V5EYPLJ14=GS1.2.1698421801.21.1.1698421821.40.0.0; epssw=1*tRN611ixQfhstFzaIA7SZ5ITHRMiILGSIAXOFklw3AbV7zFIs7hZF1B5dtJe0v626T19P_-OpxJdLyfb6T65HQ9Abh-GiX9W6UVD_9-M0olpDJJ45seqt7kZ9ECIL_HR8VVSzTH_e8B49AK3xYB4yaBBe8KpxkD53mwSetzRyTB4eNkqy2Wm6XPnLNSnet4RyTB4eKP.; isg=BHp6kGaPy858v0bjlP0ajRIfy6CcK_4FwZCLBIRzJo3YdxqxbLtOFUCBxxurQnad',
              '__wpkreporterwid_=310a2921-e0d5-431f-b10e-f547968277d7; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; xlly_s=1; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19658%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698981507%7C3%7CMCAAMB-1698981507%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698383907s%7CNONE%7CvVersion%7C5.2.0; t_sid=gdwX3sawOPW0TWqZGplZKc11Wu0HLE9l; utm_channel=NA; _m_h5_tk=9c6578c86c0843e992afac2ba4bbd5f5_1698431521727; _m_h5_tk_enc=d87ddc0b1987289827d1904f2b9e72e2; _gat_UA-30172376-1=1; _ga_3V5EYPLJ14=GS1.2.1698421801.21.1.1698421975.39.0.0; epssw=1*GRcs11g0-1hftdDMuW14MJtIh2U4urzaIAbmIHuFYObqIUFQ3bhSH962NKBxj5B5NKC9P_-OblPJpvKy6T69Fp62bhR9RjBvNZPD__S1ruw6qvJ4yQwqt7kZCUAduQKnIyxQBkD73DmnTTI3xv9-etzRyHqdeKy53mSVxDDBeDmnJLLG8DzW15XjBTB4YDmnxYBqy1..; isg=BCEhHdLf4MvzG01-07jBqO1iMO07zpXADn3AeYP2HSiH6kG8yx6lkE8sTAbsBy34']
# cookie='__wpkreporterwid_=310a2921-e0d5-431f-b10e-f547968277d7; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_cid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_uid=4841c06e-06a4-4d0b-90b2-1e8e4b7efab6; t_fv=1696921554330; lwrid=AQGLGGgN5KveRcpZH%2FFDX39uI0WJ; lazada_share_info=659577610_1_9300_530464_659577610_null; miidlaz=miidgjno221hd379eobf630; cna=0uWrHaYs+04CASpyZwc4PEw3; _bl_uid=3al2hnb1w8Or969Ie6j3m86x8nwt; _gcl_au=1.1.1862929219.1697694136; lzd_sid=1d5920aa599dd4be0de92ae5fdb1d707; _tb_token_=701f83e8e3e8e; _ga=GA1.2.1344107077.1697694193; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; exlaz=c_lzd_byr:mm_150041215_51353031_2010353111!vn1296001:clkgg5pni1hd3h0pcuapt1::; lzd_click_id=clkgg5pni1hd3h0pcuapt1; xlly_s=1; _gid=GA1.2.1196349833.1698079719; cto_bundle=rP0S6V9WQ25tZHJCVUU0RFBaWkxVbjRyaWlDa0xKekJPOTNGc3A0SHNpZmYlMkJjVzNrZlBmaFJqUzE4Tnp6VFJRaUtoV2hlQ1VBdHY0SHJ2Tk1iTFB1djJNdU9TSHdGazJxU1g1NiUyQlVqMER5ZXZ5WEYyQmo2bHhmZEtIekclMkJlWU50Yk1MNlhlVHRSMUV4SG5JZEdkeVVjYldUeHNJaGlNZDBTNURMYzFMcGhhMkk5M2tGMGVyalZjRXZCJTJGa2ZPWnBOTlY3S2xLRE1MRFMwU2tmRlk3aUZNdFNxZlElM0QlM0Q; __itrace_wid=3e42c926-56e3-4270-b359-e2e1e3de301f; _uetvid=bfc718e0126311eea8b10777b7e2fca8; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19656%7CMCMID%7C75354626526456153913021886949163663268%7CMCAAMLH-1698812900%7C3%7CMCAAMB-1698812900%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1698215300s%7CNONE%7CvVersion%7C5.2.0; t_sid=shcx0lVEeYSYxqhYDABLPygmE9q8NebH; utm_channel=NA; _m_h5_tk=659b6c5d7c72609efa8564b4b8601383_1698334921311; _m_h5_tk_enc=bc8bb804cea1de235a4c47b5538f1611; EGG_SESS=S_Gs1wHo9OvRHCMp98md7I7UyuMbdi04ZhBTtir5lFH-UZISZEA96R4eDyxSo88I2U3r_4JakpVsxCm728PUBRi4Q8DUfT5y2Ebhu41QzeF171cuPnWzP9yEW5U3Co_MOppVZaEo2F_k44K07EbSWRb5dCfzEk3pSIJ2URxbJXE=; _gat_UA-30172376-1=1; _ga_3V5EYPLJ14=GS1.2.1698327368.18.1.1698329300.60.0.0; epssw=1*MFO611iaG5FOG_GSuW_SZ-FFHRGku5b86R6As6CXIAvso4f87ubLuODNtCv_jcfOFGxGFxNnO2pidtR_NqWVdtSiep62dt7ChKv466pmTrpA6OR9F1BRNKKQFp9V-8pHneLauSTZidrFO7MZsm04-BUVZvTT-HaH3Je8dL3y7kqnyaBR3zQJyC2Cevp8hD7RyaB_CnUa3A448tmbSXDFW4yBFDVbE-onWaQRyah.; isg=BF5e7DsDt7OWh-IXGEm2YdZjr_SgHyKZBdwv0Ajn4KGAK_8FcK04qOLNIy8nShqx'
def getHeaders(num):
    headers={
    'authority' :'www.lazada.vn',
    'accept' : 'application/json, text/plain, */*',
    'accept-language' : 'en-US,en;q=0.9,vi;q=0.8',
    'cookie' : cookie_lis[num],
    'referer' :'https://www.lazada.vn/',
    'Postman-Token': 'fcbae239-7197-4bde-a38d-a0460aa8dc6c',
    'Accept-Encoding': 'gzip, deflate, br',
    "Host": 'www.lazada.vn',
    'Connection' : 'keep-alive',
    'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform':"Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-csrf-token' : '701f83e8e3e8e',
    'x-requested-with': 'XMLHttpRequest'
    }
    return headers

# Định nghĩa thông tin đăng nhập cho proxy
proxy_username = 'tester@603dc'
proxy_password = '894s1Mwxg_!?'

# Định nghĩa địa chỉ IP và cổng của proxy
proxy_url = 'http://forward.test.io:3128'


# Tạo một session cho requests và đặt proxy với đăng nhập
session = requests.Session()
session.proxies = {
    "http": proxy_url,
    "https": proxy_url,
}

# # Đặt thông tin đăng nhập cho proxy
session.proxies.update({
    "http://": f"http://{proxy_username}:{proxy_password}@{proxy_url}",
    "https://": f"https://{proxy_username}:{proxy_password}@{proxy_url}"
})


def getParams(page_num):
    params = {
        'ajax' : 'true',
        'from' : 'wangpu',
        'isFirstRequest' : 'true',
        'langFlag' : 'vi',
        'page' : {page_num},
        'pageTypeId' : 2,
        'q' : 'All-Products'
    }
    return params

def getData(shop_name, page_num, count_except):
    url  = "https://www.lazada.vn/" + shop_name
    session.headers.update(getHeaders(random.randint(0,5)))
    response = session.request("GET", url=url, params=getParams(page_num))
    if response.status_code != 200:
        print("Không thể thực hiện request!")
        sys.exit()

    try:
        res_json = response.json()
        mods = res_json["mods"]
        lisItems = mods["listItems"]
    except Exception as e:
        count_except +=1
        print(response.text)
        print("Dữ liệu trả về không đúng định dạng!")
        if count_except == 5:
          sys.exit()

        time.sleep(60)
        getData(shop_name, page_num, count_except)

    # Duyệt qua các item
    lisItemsJson = []
    for item in lisItems:
        # chuyển số lượt mua sang dạng số
        number = 0
        if "itemSoldCntShow" in item:
            itemSoldCntShow = item["itemSoldCntShow"]
            matches = re.search(r'(\d[\d,]+)|(\d)', itemSoldCntShow)
            if matches:
                # Lấy số từ kết quả tìm kiếm và loại bỏ dấu ","
                number = int(matches.group(0).replace(',', ''))
            else:
                number = 0

        originalPrice  = item["price"]
        discount = 0
        if "originalPrice" in item:
            originalPrice = item["originalPrice"]
            discount = item["discount"]

        itemJson = {
            "name" : item["name"],
            "nid" : item["nid"],
            "itemId" : item["itemId"],
            "originalPrice" : originalPrice,
            "price": item["price"],
            "discount" : discount,
            "ratingScore": item["ratingScore"],
            "review" : item["review"],
            "inStock" : item["inStock"],
            "itemSoldCntShow" : number

        }
        lisItemsJson.append(itemJson)

        # check have the next page?
        have_nPage = res_json["mainInfo"]["noMorePages"] == False
        return lisItems, have_nPage

def writeToFile(shop_name, lisItemsJson):
    fileName = shop_name +".json"
    with open(fileName, "a", encoding="utf-8") as json_file:
        json.dump(lisItemsJson, json_file, ensure_ascii=False, indent=4)

if __name__=='__main__':
    with open('list_url.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("Shop: "+row[0])
            # Biến kiểm tra có trang sản phẩm tiếp theo không
            have_nPage = True
            page_num = 0
            while have_nPage == True:
                page_num += 1
                print(f"Page: {page_num}")
                # Lấy dữ liệu
                lisItemsJson, have_nPage = getData(row[0], page_num, 0)

                # Ghi vào file
                writeToFile(row[0], lisItemsJson)
                time.sleep(random.randint(60, 120))

