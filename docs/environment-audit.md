# Phase 0 — Environment Audit

稽核日期：2026-11-25（Asia/Taipei）；主要工具與連線檢查於約 20:14–20:17 執行。本報告僅記錄環境、唯讀連線與目錄結構檢查；未開始 Phase 1，未撰寫論文，未生成 V1、V2、V3、PDF、差異檔或 Overleaf ZIP。

## 1. 已閱讀文件與工作範圍

已完整閱讀 `AGENTS.md`、`README.md`、`docs/PROJECT_CONTEXT.md`、`docs/ROADMAP.md`、`docs/ACCEPTANCE_CRITERIA.md`，並閱讀 `openspec/README.md`、`paper/README.md`、`deliverables/README.md`、`CHANGELOG.md` 與 `.gitignore`。

理解與後續執行邊界如下：

- SmartIntake 面向固定實驗室／辦公室的飲水與飲食記錄。公開文件提出 Raspberry Pi 4、兩組 Load Cell/HX711、FastAPI、PostgreSQL、Discord 與 n8n tool-grounded agent；這是研究規劃，不能視為已驗證的實作。
- 重量下降僅能構成候選事件；須處理補水、灑漏、容器更換、共享設備歸屬與確認機制。缺失資料不能當成零。
- E1–E5 的重量、事件、使用者切換、記錄負擔與 agent 評估尚無正式結果，不得宣稱已證明改善。
- DIC4 工作依序為環境稽核、IEEEtran conference V1、實際 V1 審查、依審查修訂 V2、V3 方法與證據精進、Overleaf／交付。保留各版獨立來源與 PDF，建立審查 ID、需求、差異和驗證的對應。
- 真正論文修訂前須建立並驗證 OpenSpec change，包含課程要求的 `goal.md`、`proposal.md`、`design.md`、`tasks.md` 與 delta specs。作者與研究結果不得杜撰。
- `bambamboo0321/AIOT-final` 是權威實作來源；`RayWu576/AIoT-DIC4` 僅參考結構。此次未審查私人實作，因此未新增任何「實作已完成」的判定。

## 2. 結果總覽

| 項目 | 實際結果 | 狀態／影響 |
|---|---|---|
| Git 與目前 GitHub repository | Git 2.39.5；遠端 HEAD 與本機稽核起點一致；沙箱外唯讀連線成功 | 已驗證讀取；本機 commit 缺作者設定；未測試 push |
| GitHub CLI／連接器 | `gh` 2.101.0；沙箱外認證成功；GitHub 連接器讀取成功 | 可用；沙箱內結果有差異 |
| Node.js／npm | v24.13.1／11.8.0 | 可用 |
| OpenSpec CLI／schema | CLI 不在 PATH；未初始化本 repo schema | 缺少，無法執行 change 驗證 |
| LaTeX／latexmk／BibTeX／latexdiff | 所需指令未找到 | 缺少，無法編譯或產生差異 |
| IEEEtran class／bibliography style | 無 `kpsewhich`；本 repo 無追蹤的 `.cls`／`.bst` | 未能驗證，不宣稱已安裝 |
| Overleaf MCP | 目前工具與本機 MCP 清單無 Overleaf；插件搜尋無結果 | 本工作階段不可用 |
| 私人 AIOT-final 讀取 | 連接器最小內容讀取與 Git HEAD 查詢皆成功 | 已驗證；未複製私有來源 |
| 公開參考庫 | 完整 tree、main 分支、兩個 annotated tags 可讀 | 僅完成結構檢查 |

## 3. Git、GitHub 與權限證據

### 3.1 目前工作庫

稽核起點（新增本報告前）：

```text
git status --short --branch
## main...origin/main

git remote -v
origin  https://github.com/bambamboo0321/AIoT-DIC4.git (fetch)
origin  https://github.com/bambamboo0321/AIoT-DIC4.git (push)

git rev-parse HEAD refs/remotes/origin/main
519b5557e8d86503db17d97640c0b847f5d1d31c
519b5557e8d86503db17d97640c0b847f5d1d31c
```

起點工作樹乾淨；本機分支為 `main`，追蹤 `origin/main`；`git rev-list --count HEAD` 為 14；`git tag --list` 無輸出。尚無本專題的 V1／V2／V3 標籤。`git ls-files '*.tex' '*.bib' '*.pdf' '*.zip' '*.cls' '*.bst'` 無輸出。

執行 `git ls-remote --exit-code origin HEAD refs/heads/main`：

| 執行環境 | Exit code | 觀察 |
|---|---:|---|
| 預設沙箱內 | 128 | `Could not resolve host: github.com` |
| 經核准的沙箱外唯讀重試 | 0 | HEAD 與 `refs/heads/main` 均為上述 `519b5557…` |

`gh auth status` 在沙箱內 exit 1，回報登入失敗；沙箱外重試 exit 0，回報 `bambamboo0321` 透過 keyring 登入成功。兩次結果不同，不能把沙箱內失敗直接解讀為憑證失效；本次未重新登入或改寫認證設定。

GitHub 連接器的 repository metadata 查詢也成功，確認目前 repository 為 public、default branch 為 `main`，並回報 pull／push 權限。權限欄位不等於實際寫入驗證；本次沒有 push、遠端寫入或發布。

報告完成並通過 `git diff --cached --check` 後，依 `AGENTS.md` 嘗試建立獨立本機提交：`git commit -m 'docs: record Phase 0 environment audit'`。該操作 exit 128，回報 `Author identity unknown`，因此**沒有建立 commit**。補查 `git config --get user.name` 與 `git config --get user.email` 均 exit 1、無設定值。未自行填入身分或變更 Git 設定；本報告保留在本機暫存區，需使用者提供提交身分後才能提交。

### 3.2 權威私人實作庫

經目前已連接的 GitHub 授權進行以下唯讀檢查：

1. 精確搜尋 `repo:bambamboo0321/AIOT-final`：成功，回報 private、default branch `main`、`pull: true`。
2. 使用連接器讀取 `README.md` 第 1 行：成功回傳非空內容；只記錄成功與否，不將內容寫入此公開 repo。
3. 沙箱外執行 `git ls-remote --exit-code https://github.com/bambamboo0321/AIOT-final.git HEAD`：exit 0，成功回傳 HEAD。

結論：本次授權下的連接器與 Git 讀取路徑均可用。未 clone、未複製私人原始碼、未保存私人 README 內容，亦未驗證實作或實驗結果。報告省略私人 HEAD 與內容細節。

## 4. 本機工具版本與失敗紀錄

環境：macOS 26.2、Apple Silicon arm64、zsh。

| 工具／指令 | 實際版本或結果 | Exit code／備註 |
|---|---|---|
| `git --version` | `git version 2.39.5 (Apple Git-154)` | 0；`/usr/bin/git` |
| `node --version` | `v24.13.1` | 0；由 nvm 管理 |
| `npm --version` | `11.8.0` | 0；與上述 Node 相同版本目錄 |
| `gh --version` | `2.101.0 (2026-09-15)` | 0 |
| `brew --version` | `Homebrew 7.0.9` | 0 |
| `codex --version` | `codex-cli 0.171.0-alpha.13.2` | 0；另有 PATH alias 建立權限警告 |
| `openspec --version` | `command not found: openspec` | 127 |
| `latex --version` | `command not found: latex` | 127 |
| `pdflatex --version` | `command not found: pdflatex` | 127 |
| `latexmk -v` | `command not found: latexmk` | 127 |
| `bibtex --version` | `command not found: bibtex` | 127 |
| `latexdiff --version` | `command not found: latexdiff` | 127 |
| `kpsewhich IEEEtran.cls` | `command not found: kpsewhich` | 127；class 無法定位 |
| `kpsewhich IEEEtran.bst` | `command not found: kpsewhich` | 127；style 無法定位 |
| `xelatex`／`lualatex`／`tlmgr` | PATH 查找未找到 | 未取得版本 |

補充檢查：

- `/Library/TeX/texbin` 與 `/usr/local/texlive` 均不存在。這支持目前沒有可用的標準 MacTeX 工具鏈，但不代表已遍歷整台電腦尋找所有自訂安裝位置。
- 全域 `npm ls -g --depth=0 --json` exit 0，僅列出 `corepack 0.34.6` 與 `npm 11.8.0`，沒有 OpenSpec。
- `node_modules/.bin/openspec`、`/opt/homebrew/bin/openspec`、`~/.local/bin/openspec`、`openspec/config.yaml`、`openspec/config.yml` 均不存在。repo 根目錄無 `package.json`／`package-lock.json`。
- Codex 指令回報 `could not create PATH aliases: Operation not permitted (os error 1)`；版本與 MCP 清單仍成功返回。本次未變更 PATH 或全域設定。

### OpenSpec 邊界

`openspec/README.md` 明定 Phase 0 先檢查已安裝 CLI，依其支援 schema 初始化後才建立 changes。目前 CLI 缺少，故本次僅新增 Phase 0 稽核紀錄；未手寫猜測 schema、未建立論文 change、未執行 `openspec validate`，也未宣稱任何驗證或 archive 成功。此項是進入真正論文修訂前必須解決的前置缺項。

### LaTeX 邊界

沒有可用編譯器、文獻工具與 IEEEtran 定位工具，因此本次沒有 compiler log、BibTeX 結果、版面檢查或 latexdiff 成功證據。不能將參考庫內存在 PDF 視為本機編譯成功。

## 5. MCP 與 Overleaf

檢查兩種來源，避免把本機 CLI 設定與目前工作階段的連接器混為一談：

1. **本機設定**：`codex mcp list --json` exit 0。僅擷取 server 名稱、enabled、transport type、auth status；未輸出完整設定、環境變數或認證內容。
2. **目前工作階段**：查詢已提供的工具目錄，並透過 Plugin Management 搜尋 `Overleaf`。

本機 MCP 清單：

| Server | Enabled | Transport | 回報的 auth status |
|---|---|---|---|
| `codex_app` | false | stdio | unsupported |
| `cua_repl` | true | stdio | unsupported |
| `node_repl` | true | stdio | unsupported |

`unsupported` 是清單中的狀態值，不等於 server 已通過健康檢查或已失效；本次沒有額外啟動各 server 測試。工作階段另有 GitHub、Plugin Management 等連接器工具，其可用性由實際讀取／搜尋操作驗證；不能僅因本機 `codex_app` disabled 就判定這些工具不可用。

Overleaf 結果：

- 目前工具目錄中，名稱與描述均未發現 Overleaf 工具。
- 本機上述 MCP 設定無 Overleaf server。
- Plugin Management 的 `Overleaf` 搜尋成功，回傳空清單 `plugins: []`。這只代表此次搜尋未找到可用插件，不代表所有外部整合均不存在。
- 結論：本次工作階段無可呼叫的 Overleaf MCP；未執行 Overleaf 專案讀取、編輯、同步或編譯，也沒有相關成功證據。
- n8n research agent 不等於 Overleaf manuscript tooling，不能替代此項驗證。

後續若配置 Overleaf MCP，須在授權專案上實測並留下去識別化證據。若仍不可用，依 roadmap 在後續交付階段提供本機獨立編譯、解壓與匯入檢查過的 ZIP；目前工具鏈缺少且使用者限定 Phase 0，因此此次未產生或宣稱已測試 ZIP。

## 6. 公開參考庫的目錄與版本結構

來源：[RayWu576/AIoT-DIC4](https://github.com/RayWu576/AIoT-DIC4)。使用 GitHub 連接器讀取 metadata、遞迴 Git tree、branches、tag refs 與 annotated tag objects，未下載或沿用其論文內容與實驗資料。

- repository：public；default branch：`main`。
- branches 查詢僅回傳 `main`；稽核時 HEAD 為 `e1852cb65206135dad261abeeb063ee628362f40`。
- 遞迴 tree 回報 `truncated: false`，共有 59 個檔案與 26 個目錄項目。
- 以下為結構摘要，`…` 表示省略的已觀察路徑，並非實際檔名。

```text
README.md
.gitignore
paper/
  v1-initial/
    main.tex, preamble.tex, references.bib
    figures/{board,system,workflow}.tex
    sections/{abstract,conclusion,evaluation,introduction,related,scheme}.tex
  v2-revised/
    main.tex, preamble.tex, references.bib
    figures/…
    sections/…
deliverables/
  DIC4_Conference_V1_Initial.pdf
  DIC4_Conference_V2_Revised.pdf
  DIC4_Conference_V1_V2_Diff.pdf
  Overleaf_V1.zip
  Overleaf_V2.zip
openspec/
  config.yaml
  changes/
    dic4-ieee-conference-paper/{proposal.md,design.md,tasks.md,specs/…}
    revise-ieee-conference-paper/{proposal.md,design.md,tasks.md,specs/…}
    archive/.gitkeep
  specs/.gitkeep
reviews/
  v1-review.md
  revision-report.md
research/
  citation-mapping.md
  claim-evidence-map.md
  research-gaps.md
experiments/
  README.md
  evaluation-plan.md
  preliminary-results.csv
docs/
  build-instructions.md
  overleaf-setup.md
  publication.md
  validation.md
  verify-and-package.ps1
```

版本標籤的實際解析結果：

| Tag | Annotated tag object | 指向的 commit |
|---|---|---|
| `v1.0-initial-draft` | `cbf76885290b8c71ebcbe3425fce59e7fadd1687` | `c1550b405821b4f5c9487e47db7820c359297e6e` |
| `v2.0-revised-draft` | `82b42ad7318c8ed5ec1144d998ed420cfc2e4082` | `bb5552c7f03b6fdc3443b59b39fcabf53144c659` |

在本次完整 tree 與 tag refs 中未見 V3。`archive/` 僅有 `.gitkeep`，不能宣稱參考庫的 changes 已完成歸檔；兩個 change 的已觀察路徑未見 `goal.md`，不能直接視為符合本 repo 額外的課程要求。

可借用的只有組織方式：獨立來源快照、分開的 PDF／ZIP／Diff、審查與修訂對應，以及研究證據目錄。本次沒有開啟其 PDF／ZIP、驗證其編譯、審核其研究結論或移植任何結果。`verify-and-package.ps1` 的存在僅是結構觀察，尚未評估能否在本機 macOS 執行。

查詢失敗也保留紀錄：GitHub 連接器拒絕 `/tags?per_page=100`（HTTP 400，endpoint 不在該工具允許清單）。改用受支援的 `/git/matching-refs/tags/` 成功取得兩個 refs，再讀取 tag objects 解析 commit；前一次錯誤不代表 repository 無標籤或無讀取權限。

## 7. 缺少項目、建議處理方式與問題

以下僅為建議；**本次沒有安裝依賴或變更全域設定**。執行安裝與設定前須另取得使用者核准。

| 優先項目 | 建議方式（未執行） | 後續須驗證／可能問題 |
|---|---|---|
| OpenSpec CLI | 可用目前 npm 安裝；官方示例：`npm install -g @fission-ai/openspec@latest`。安裝前核定目標版本 | 記錄實際版本與 help，依已安裝 schema 初始化；nvm 切換 Node 後全域 CLI 可能不在 PATH |
| LaTeX 工具鏈 | macOS 可選完整無 GUI 發行版：`brew install --cask mactex-no-gui` | 下載與磁碟需求較大；可能需要管理員權限；安裝後開新終端以載入路徑 |
| IEEEtran、latexmk、BibTeX、latexdiff | 工具鏈安裝後逐一查驗；缺包時再依已安裝發行版的 package manager 補齊 | 不預先宣稱 class、style 或程式可用；檢查 `kpsewhich IEEEtran.cls`／`IEEEtran.bst` 與各版本指令 |
| Overleaf MCP | 先確認欲採用的 server、配置方式與授權專案，再核准連接；此次未找到可直接使用的整合 | 需實際讀取與後續獲授權操作的證據；不得以 n8n 代替 |
| 沙箱網路／認證限制 | 保留連接器或經核准的沙箱外唯讀路徑 | 不必因沙箱內錯誤重設 token；每次區分連接器、Git 與沙箱的狀態 |
| Git commit 作者設定 | 使用者提供提交姓名與 Email 後，可核准設定本 repo 的 `user.name`／`user.email` | 目前 commit 因缺少身分失敗；不使用推測身分、不修改全域設定 |
| OpenSpec 工作流程 | CLI 可用後，先檢視已安裝 schema，再建立第一個真正論文修訂 change | 課程另要求 `goal.md`；不能照抄參考庫或補造通過驗證紀錄 |

OpenSpec 目前官方 npm 安裝說明要求 Node.js 至少 22.20.0；已觀察的 v24.13.1 符合此門檻，但這不等於 CLI 已安裝或本機已驗證相容。安裝方式與版本須以實際執行時的官方說明為準。[OpenSpec 官方安裝文件](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md)

MacTeX 無 GUI cask 的安裝指令與終端重啟說明已查核。[Homebrew 官方 mactex-no-gui 頁面](https://formulae.brew.sh/cask/mactex-no-gui)

額外來源失敗：本次網頁工具存取 `https://tug.org/mactex/` 回報 HTTP 403；未把該頁視為成功讀取，MacTeX 安裝建議採用上述可成功存取的 Homebrew 官方頁面。

## 8. Phase 0 完成狀態與下一階段阻礙

- [x] 完整閱讀指定五份文件，確認 SmartIntake、DIC4、版本流程與證據界線。
- [x] 檢查 Git 狀態、遠端、實際版本與 GitHub 唯讀連線，區分沙箱內外結果。
- [x] 檢查 Node/npm、OpenSpec、LaTeX／IEEEtran／latexmk／BibTeX／latexdiff，保留缺項與失敗。
- [x] 檢查 MCP 設定、工作階段工具與 Overleaf 插件搜尋結果。
- [x] 驗證私人 AIOT-final 最小讀取權限；未複製私人內容。
- [x] 檢查公開參考庫的完整目錄與實際版本標籤。
- [x] 將結果、建議方式與可能問題保存至本報告。
- [ ] OpenSpec CLI 安裝、schema 初始化與實際 change 驗證：未執行。
- [ ] LaTeX、IEEEtran、文獻與差異工具可用性：缺少／未能驗證。
- [ ] Overleaf MCP 授權操作：目前不可用；ZIP fallback 於後續階段處理。
- [ ] 本機獨立 commit：已嘗試但因缺少 Git 作者設定失敗；報告已保存並暫存。

Phase 0 的稽核與紀錄已完成，環境尚未就緒。此次新增交付物只有本報告，未修改論文來源或推送／發布內容。停在 Phase 0，等待使用者審閱與下一階段指令。
