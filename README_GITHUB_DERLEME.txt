GOBEKLI TEPE - GITHUB'TA BSP DERLEME
====================================

Bu yöntem PC'ye compiler kurmaz. Haritayı GitHub Actions derler.

1) Bu klasörün İÇİNDEKİ dosyaları yeni/boş bir GitHub reposunun köküne yükle.
   .github klasörünün de GitHub'a gittiğinden emin ol.

2) GitHub reposunda "Actions" sekmesine gir.

3) Solda "Build Gobekli Tepe BSP" workflow'unu seç.

4) "Run workflow" > "Run workflow" ile başlat.
   Push yaptıktan sonra otomatik de başlayabilir.

5) İşlem yeşil tik olunca çalışmanın sayfasını aç.
   En alttaki "Artifacts" bölümünden:
       fy_gobeklitepe_v12-BSP
   dosyasını indir.

6) İndirilen ZIP'i aç. İçindeki:
       fy_gobeklitepe_v12.bsp
   dosyasını bu klasörde BSP_KUR_VE_AC.bat yanına koy.

7) BSP_KUR_VE_AC.bat dosyasına sağ tık > Yönetici olarak çalıştır.

8) CS otomatik açılmazsa konsola:
       map fy_gobeklitepe_v12

Not:
Bu yöntem derlemeyi GitHub'ın Windows sunucusunda yaptığı için yerel PowerShell,
VHLT kurulumu ve Program Files yazma problemi derleme aşamasında devreden çıkar.
