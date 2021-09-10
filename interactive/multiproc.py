# pylint: skip-file

#%%
import sys, os

sys.path.append(os.path.abspath(os.path.join("src")))
# sys.path.append(os.path.abspath(os.path.join("..", "src")))

import subprocess
import json

import tqdm

from common.app import App
from common.api import Api
from common.database import Database
from common.helpers import Helpers
from common.insertor import InsertFromJsonl

app = App()
api = Api()
db_test = Database("test.db", api.app)
db_tweets = Database("tweets.db", api.app)
insertor = InsertFromJsonl(api.app)

jsonl_path = os.path.join(app.root_dir, "database", "jsonl")
test_file = "UN_flat_test.jsonl"
jsonl_file_flat = os.path.join(jsonl_path, "flat", test_file)

with open(jsonl_file_flat) as jsonl_flat:
    tws_flat = [json.loads(line) for line in jsonl_flat]

with db_test:
    tws_db = db_test.get_all_tweets()

num_tweets = insertor.get_tot_lines(test_file)

# UN db hashes with problem
prob_idx = [
    "2797333945",
    "1150376771",
    "1264486216",
    "3776111979",
    "7348529822",
    "8060968710",
    "8425152998",
    "1369319545",
    "2407676646",
    "1553380150",
    "1301402049",
    "8364295167",
    "2321291292",
    "9254163372",
    "9612893210",
    "1251706049",
    "5172653799",
    "9328975593",
    "3904825561",
    "5884374597",
    "1456717502",
    "5705677631",
    "1256357310",
    "7121297876",
    "4750568587",
    "1172829019",
    "9885298262",
    "2550355338",
    "5653541928",
    "1079304734",
    "1322482685",
    "1331891243",
    "1035803472",
    "3041373352",
    "1004618301",
    "1376241740",
    "1306316366",
    "2064817447",
    "6677396735",
    "8923687482",
    "9219223686",
    "1760115169",
    "9770582618",
    "1318675788",
    "6806489575",
    "4600807805",
    "1317155192",
    "1402864371",
    "7553614812",
    "7960446752",
    "1135395513",
    "1921839917",
    "1026010172",
    "7758045795",
    "2716318786",
    "6647175364",
    "1408323780",
    "1005515099",
    "1578204830",
    "6017050253",
    "1188910095",
    "7916684958",
    "9314139896",
    "1293878048",
    "8597319179",
    "8896522569",
    "1081883602",
    "6038697284",
    "1423114417",
    "5724536290",
    "2702882390",
    "1359433667",
    "3236487486",
    "3771781630",
    "5384133344",
    "8248857217",
    "1306699041",
    "1045914426",
    "4160713221",
    "1560723392",
    "2920400120",
    "1202501149",
    "1394277943",
    "4134442752",
    "1102021372",
    "3180889412",
    "1017081195",
    "3061539261",
    "3771192283",
    "8217768796",
    "9600189080",
    "4711216700",
    "1011206463",
    "2877477057",
    "4456326352",
    "9937496257",
    "3862767084",
    "4710413135",
    "1008319299",
    "1072644864",
    "1205255953",
    "2696445409",
    "2871958557",
    "6617833649",
    "1738838762",
    "1802981524",
    "7500085521",
    "2226614767",
    "6883668912",
    "8400827935",
    "1113160060",
    "1157527615",
    "8492188200",
    "1073995504",
    "2196324797",
    "4687268458",
    "9109800536",
    "8066477273",
    "1415591650",
    "1149974927",
    "4983318939",
    "1750852673",
    "4467927335",
    "1127968451",
    "7927377993",
    "1376806485",
    "3747756077",
    "1327409213",
    "4947167996",
    "1034977918",
    "1681165265",
    "4073859079",
    "1073341256",
    "8256114318",
    "8259821592",
    "1500670485",
    "2635865932",
    "1105683472",
    "5468048088",
    "8827858406",
    "1297690960",
    "4015771260",
    "4772085279",
    "1307583631",
    "9823818618",
    "4875629411",
    "2062368615",
    "7680200321",
    "1286492991",
    "2672498335",
    "8953613886",
    "6227750548",
    "5979491293",
    "4683229813",
    "4988714202",
    "6729508941",
    "2503746968",
    "1276032707",
    "1113295159",
    "2117197347",
    "2461619679",
    "1297837417",
    "3990914677",
    "1051655083",
    "1251026734",
    "8867923849",
    "2749262616",
    "6409989933",
    "1357002506",
    "1355919099",
    "1220744071",
    "4270119126",
    "1499139430",
    "2449621787",
    "1102770432",
    "9631261718",
    "1397125177",
    "1333135315",
    "1872644866",
    "2627498586",
    "2727127238",
    "1431893044",
    "2670349949",
    "6953957862",
    "1842028036",
    "1413748019",
    "2970544214",
    "1147898172",
    "4897563437",
    "1712936284",
    "7788753228",
    "8397623324",
    "1059436951",
    "7548680707",
    "1238211134",
    "1414434323",
    "1195599034",
    "2094864405",
    "5673647730",
    "1231584973",
    "3791767411",
    "1379522367",
    "1979675882",
    "2857419492",
    "9765223306",
    "1152836612",
    "5266141870",
    "1055256931",
    "8212771854",
    "3271738278",
    "5179701873",
    "4507701885",
    "1306299598",
    "1360384452",
    "2734603853",
    "1453049770",
    "5023594183",
    "8222059929",
    "1044473303",
    "8711980515",
    "7685201171",
    "1333421987",
    "6436670930",
    "1194700395",
    "4183539778",
    "5697844496",
    "5302152606",
    "6112221925",
    "7005093763",
    "1158340422",
    "6073274411",
    "1463030116",
    "1319847333",
    "5556664967",
    "4199727636",
    "2386273858",
    "1292022626",
    "4453458163",
    "3718482164",
    "1010346656",
    "1108251616",
    "3174313444",
    "9108217836",
    "9860031453",
    "1043287189",
    "5130369889",
    "5835249760",
    "5135659418",
    "2987555867",
    "1008487828",
    "1426581097",
    "1142125984",
    "1391349565",
    "2054965036",
    "1010425655",
    "6002153219",
    "1208576164",
    "5162616090",
    "5374439595",
    "3459216676",
    "3565250877",
    "4680255219",
    "5796781552",
    "6581990898",
    "4593859850",
    "1361959473",
    "5104434548",
    "2001804808",
    "2869688523",
    "1166877205",
    "4173607584",
    "1318605796",
    "1039989206",
    "1003469935",
    "6949732153",
    "1027962447",
    "1071661191",
    "4791284254",
    "3605459402",
    "2801535419",
    "1213202275",
    "2302578882",
    "2437295819",
    "1061645340",
    "9765252801",
    "5998746188",
    "6808313057",
    "1929565416",
    "7431011236",
    "1879302577",
    "4272388954",
    "2824278579",
    "4169281749",
    "5746587120",
    "2964596208",
    "3888030506",
    "2130177811",
    "1561474771",
    "2777299478",
    "5109110950",
    "7480017153",
    "8531513136",
    "9091219809",
    "3370999935",
    "5405396475",
    "2404890196",
    "6222690317",
    "3083478706",
    "1332073708",
    "8309533503",
    "1431790212",
    "2441037668",
    "1346848814",
    "1115028514",
    "1138585210",
    "3692209633",
    "3045885046",
    "8743502053",
    "1447585778",
    "8956022739",
    "3010408115",
    "4318582657",
    "7428466600",
    "1059534944",
    "1288709827",
    "7306259653",
    "1243885597",
    "1392453895",
    "1364079644",
    "4887446896",
    "7256969822",
    "9163917087",
    "3975113791",
    "7899746294",
    "1376907293",
    "1117878458",
    "1492161959",
    "6158743461",
    "2226654395",
    "4624196145",
    "9762847943",
    "7711304544",
    "1015155683",
    "1123699063",
    "1327767311",
    "8137388462",
    "7514472481",
    "4166972677",
    "1349156780",
    "6955407342",
    "7619916019",
    "7253095677",
    "1013820748",
    "4381759739",
    "1247786472",
    "1481890311",
    "3857990180",
    "4737965822",
    "1223883994",
    "1127118595",
    "5940809585",
    "1451376456",
    "1388648093",
    "2327465128",
    "1450662963",
    "4367565797",
    "1170486745",
    "1285508981",
    "2593424219",
    "6954745376",
    "6450001218",
    "5967033731",
    "8794907443",
    "4026242500",
    "8089193778",
    "4527647602",
    "1357473889",
    "9232776124",
    "5644452991",
    "9550758880",
    "1411808057",
    "3701018510",
    "6069000086",
    "1425870432",
    "1026791167",
    "9056224525",
    "6246115806",
    "1009233336",
    "7602820762",
    "7428508904",
    "3548870494",
    "1152684733",
    "1682630726",
    "5351127494",
    "6356975471",
    "1448347409",
]
with db_tweets:
    prob_tweets_db = [db_tweets.get_tweet_by_id(tweet_id) for tweet_id in prob_idx]

with db_tweets:
    tws_all = db_tweets.get_all_tweets()
df = Helpers.df_from_db(tws_all)
df_UN = df[(df["handle"] == "@UN") & (df["url"] == "0")]  # 494 UN tweets have an issue

# Add tweet from tws_flat into prob_tweets_db to have at least 1 match
fake_tw = (
    "123",
    0,
    "00/00/0000",
    "@UN",
    "United Nations",
    None,
    tws_flat[0]["text"],
    "0",
    "New",
    None,
    None,
    None,
    None,
    None,
    None,
    "0",
)
prob_tweets_db.append(fake_tw)
tws_all.insert(0, fake_tw)
#%%
# Prep a few funcs


def sanitize(txt: str):
    return txt[:140].replace("\n", "").replace(" ", "") if txt is not None else None


def check_in_db(tw_flat):
    # print("check_in_db")

    # tws = tws_db  # Test
    tws = prob_tweets_db  # Prob tweets
    # tws = tws_all  # All tweets
    # tws = tws_all[:20_000]  # 20k tweets

    for tw_db in tws:
        old_id = tw_db[0]
        old_text = sanitize(tw_db[5])
        text = sanitize(tw_db[6])
        old_url = tw_db[7]
        flat_txt = sanitize(tw_flat["text"])

        # print(old_text)
        # print(new_txt)
        # print(old_text == new_txt)
        # print(len(old_text))

        if old_url == "0" and flat_txt in (old_text, text):
            new_id = tw_flat["id"]
            new_url = Helpers.build_tweet_url(new_id, tw_flat["author"]["username"])
            new_created_at = Helpers.twitter_to_db_time(tw_flat["created_at"])

            new_tweet = (new_id, new_url, new_created_at, old_id)

            # print(new_tweet)
            return new_tweet


#%%
# Multiprocessing
import multiprocessing
from tqdm.contrib.concurrent import process_map
import time

if __name__ == "__main__":
    # From 23min down to 6min30s!

    # print("Multiproc")
    # start = time.time()

    # with multiprocessing.Pool() as pool:
    #     up = process_map(check_in_db, tws_flat, chunksize=10)
    # up = [el for el in up if el is not None]

    # for tw in up:
    #     print(tw)

    # print(len(up))
    # print(f"Took {time.time() - start}s")

    print("Serial")
    start = time.time()
    to_update = [
        check_in_db(tw_flat)
        for tw_flat in tqdm.tqdm(tws_flat)
        if check_in_db(tw_flat) is not None
    ]
    print("\n", to_update)
    print(len(to_update))
    print(f"Took {time.time() - start}s")
