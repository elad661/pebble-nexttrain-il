# coding=utf-8
stations = [{"name": "Ako", "id": "1500", "lat": "32.9283231", "lon": "35.0828432"},
            {"name": "Ashdod-Ad Halom (M.Bar Kochva)", "id": "5800", "lat": "31.7739504", "lon": "34.6662706"},
            {"name": "Ashkelon", "id": "5900", "lat": "31.6759340", "lon": "34.6044924"},
            {"name": "Atlit", "id": "2500", "lat": "32.6928412", "lon": "34.9403121"},
            {"name": "Bat Yam-Komemiyut", "id": "4690", "lat": "32.0008121", "lon": "34.7594254"},
            {"name": "Bat Yam-Yoseftal", "id": "4680", "lat": "32.0145796", "lon": "34.7620815"},
            {"name": "Be'er Sheva-Center", "id": "7320", "lat": "31.2430764", "lon": "34.7983837"},
            {"name": "Be'er Sheva-North/University", "id": "7300", "lat": "31.2621399", "lon": "34.8093815"},
            {"name": "Be'er Ya'akov", "id": "5300", "lat": "31.9324674", "lon": "34.8302900"},
            {"name": "Ben Gurion Airport", "id": "8600", "lat": "32.0004345", "lon": "34.8704521"},
            {"name": "Bet Shemesh", "id": "6300", "lat": "31.7577236", "lon": "34.9875712"},
            {"name": "Bet Yehoshu'a", "id": "3400", "lat": "32.2626037", "lon": "34.8602330"},
            {"name": "Binyamina", "id": "2800", "lat": "32.5146342", "lon": "34.9500784"},
            {"name": "Bne Brak", "id": "4100", "lat": "32.1029180", "lon": "34.8302241"},
            {"name": "Caesarea-Pardes Hana", "id": "2820", "lat": "32.4852609", "lon": "34.95417"},
            {"name": "Dimona", "id": "7500", "lat": "31.0690977", "lon": "35.01175"},
            {"name": "Hadera-West", "id": "3100", "lat": "32.4383796", "lon": "34.8993350"},
            {"name": "Haifa Center-HaShmona", "id": "2100", "lat": "32.8222556", "lon":"34.9974798"},
            {"name": "Haifa-Bat Galim", "id": "2200", "lat": "32.8303311", "lon": "34.9819163"},
            {"name": "Haifa-Hof HaKarmel (Razi`el)", "id": "2300", "lat": "32.7935137", "lon": "34.9574570"},
            {"name": "Hertsliya", "id": "3500", "lat": "32.1639097", "lon": "34.8174194"},
            {"name": "Hod HaSharon-Sokolov", "id": "9200", "lat": "32.1703688", "lon": "34.9013263"},
            {"name": "Holon Junction", "id": "4640", "lat": "32.0369515", "lon": "34.7760357"},
            {"name": "Holon-Wolfson", "id": "4660", "lat": "32.0356162", "lon": "34.7595849"},
            {"name": "Hutsot HaMifrats", "id": "1300", "lat": "32.8094005", "lon": "35.0544169"},
            {"name": "Jerusalem-Biblical Zoo", "id": "6500", "lat": "31.7448338", "lon": "35.1781123"},
            {"name": "Jerusalem-Malha", "id": "6700", "lat": "31.7477545", "lon": "35.1882146"},
            {"name": "Kfar Habad", "id": "4800", "lat": "31.9923392", "lon": "34.8538735"},
            {"name": "Kfar Sava-Nordau (A.Kostyuk)", "id": "8700", "lat": "32.1677332", "lon": "34.9161099"},
            {"name": "Kiryat Gat", "id": "7000", "lat": "31.6031485", "lon": "34.7779276"},
            {"name": "Kiryat Hayim", "id": "700", "lat": "32.8248135", "lon": "35.0642744"},
            {"name": "Kiryat Motzkin", "id": "800", "lat": "32.8329986", "lon": "35.0700930"},
            {"name": "Lehavim-Rahat", "id": "8550", "lat": "31.3697891", "lon": "34.7980552"},
            {"name": "Lev HaMifrats", "id": "1220", "lat": "32.7938724", "lon": "35.0370590"},
            {"name": "Lod", "id": "5000", "lat": "31.9467808", "lon": "34.8766841"},
            {"name": "Lod-Gane Aviv", "id": "5150", "lat": "31.9670476", "lon": "34.8787312"},
            {"name": "Modi'in-Center", "id": "400", "lat": "31.9012099", "lon": "35.0057199"},
            {"name": "Nahariya", "id": "1600", "lat": "33.0052506", "lon": "35.0985393"},
            {"name": "Netanya", "id": "3300", "lat": "32.3199708", "lon": "34.8693981"},
            {"name": "Netivot", "id": "9650", "lat": "31.4111815", "lon": "34.5718847"},
            {"name": "Ofakim", "id": "9700", "lat": "31.321253", "lon": "34.6333655"},
            {"name": "Pa'ate Modi'in", "id": "300", "lat": "31.8935739", "lon": "34.9607239"},
            {"name": "Petah Tikva-Kiryat Arye", "id": "4170", "lat": "32.1061852", "lon": "34.8630665"},
            {"name": "Petah Tikva-Segula", "id": "4250", "lat": "32.1120687", "lon": "34.9009094"},
            {"name": "Ramla", "id": "5010", "lat": "31.9294538", "lon": "34.8766247"},
            {"name": "Rehovot", "id": "5200", "lat": "31.9091261", "lon": "34.8073669"},
            {"name": "Rishon LeTsiyon-HaRishonim", "id": "9100", "lat": "31.9488540", "lon": "34.8030803"},
            {"name": "Rishon LeTsiyon-Moshe Dayan", "id": "9800", "lat": "31.9875177", "lon": "34.7571751"},
            {"name": "Rosh Ha'Ayin-North", "id": "8800", "lat": "32.1207426", "lon": "34.9346832"},
            {"name": "Sderot", "id": "9600", "lat": "31.5157535", "lon": "34.585637"},
            {"name": "Tel Aviv-HaHagana", "id": "4900", "lat": "32.0543016", "lon": "34.7849715"},
            {"name": "Tel Aviv-HaShalom", "id": "4600", "lat": "32.0735594", "lon": "34.7931642"},
            {"name": "Tel Aviv-Savidor Center", "id": "3700", "lat": "32.0842437", "lon": "34.7983117"},
            {"name": "Tel Aviv-University", "id": "3600", "lat": "32.1037064", "lon": "34.8046101"},
            {"name": "Yavne-East", "id": "5410", "lat": "31.8618172", "lon": "34.7441981"},
            {"name": "Yavne-West", "id": "9000", "lat": "31.8910072", "lon": "34.7313796"}]
by_id = {station["id"]: station["name"] for station in stations}
