# Laporan Progres: Konversi Knowledge Graph (KG) ke LangGraph

## 1. Ringkasan Eksekutif
Pada tahap ini, kita telah berhasil mengeksekusi pipeline ekstraksi dan generasi kode untuk framework **LangGraph**. Skrip `src/langgraph/run.py` digunakan untuk membaca file *Knowledge Graph* berformat `.ttl` (Turtle) dari direktori `kgs_extended/LangGraph/` dan mengonversinya menjadi proyek Python yang dapat dieksekusi berbasis LangGraph.

## 2. Proses dan Metodologi
- **Input**: File-file `.ttl` dari berbagai jenis agen (contoh: *chat-agent*, *email-agent*, *supervisor*, dll) yang mendeskripsikan arsitektur dan relasi antar komponen agen.
- **Skrip Eksekusi**: Perintah dijalankan secara massal (batch process) menggunakan skrip generasi `src/langgraph/run.py`.
- **Output**: Direktori proyek terpisah di dalam `output_files/langgraph/` yang memuat logika *StateGraph*, integrasi *tools*, dan konfigurasi dependensi.

## 3. Hasil Analisis dan Generasi
Dari 9 file input KG yang diproses, **8 berhasil** dikonversi tanpa masalah, sedangkan **1 mengalami kendala**.

### 3.1 Proyek yang Berhasil Dibuat
Berikut adalah daftar 8 pola LangGraph yang berhasil digenerasi:
1. `chat-agent` (Pattern: linear)
2. `email-agent` (Pattern: tool_calling)
3. `open-code` (Pattern: tool_calling)
4. `pizza-orderer` (Pattern: tool_calling)
5. `stockbroker` (Pattern: tool_calling)
6. `supervisor` (Pattern: tool_calling)
7. `trip-planner` (Pattern: tool_calling)
8. `writer-agent` (Pattern: tool_calling)

### 3.2 Struktur Kode yang Dihasilkan
Masing-masing proyek (contoh pada `chat-agent`) telah sukses merumuskan struktur standar:
- `main.py`: Memuat implementasi `StateGraph` LangGraph, termasuk inisialisasi `AgentState`, deklarasi `nodes`, `edges`, serta pengaturan LLM (ChatOpenAI) dan *System Prompts* hasil terjemahan ontologi.
- `manifest.json`: Berisi metadata pola, nama framework, dan *timestamp* pembuatan.
- `requirements.txt`: Dependensi yang dibutuhkan (contoh: `langgraph`, `langchain-openai`).
- `.env.example`: Template *environment variables* (untuk kunci API).
- `config/inputs.yaml`: Template parameter input agent.

### 3.3 Isu / Kendala Saat Generasi Kode
Satu file gagal diproses, yaitu **`utils_instances.ttl`**. 
- **Penyebab**: Terdapat *syntax error* saat melakukan *parsing* dengan pustaka `rdflib` (`rdflib.plugins.parsers.notation3.BadSyntax`). Error terjadi saat parser mendeteksi titik (`.`) atau struktur format Turtle yang tidak valid di akhir *statement* ontologi.
- **Tindak Lanjut**: File `utils_instances.ttl` perlu diperiksa kembali sintaksnya di tahap pembersihan/validasi KG sebelum diumpankan ke *generator* LangGraph.

## 4. Pengujian Eksekusi (Runtime Validation)
Setelah proses generasi berhasil, dilakukan pengujian eksekusi (menjalankan `main.py`) terhadap 8 agen LangGraph yang dihasilkan pada *environment local* `agento-env`. Kunci API OpenAI juga telah disematkan (sebagai `OPENAI_API_KEY`) ke masing-masing eksekusi.

### 4.1 Hasil Pengujian
Sebagian besar agen sukses dijalankan dan menunjukkan respons yang valid dari model LLM:
- **`chat-agent`**: Sukses mengeksekusi LLM secara langsung (Linear) dengan respons: *"Of course! Please provide the question or topic you'd like assistance with..."*
- **`email-agent`**: Sukses memanggil fungsi eksternal (*tool calling*). Agen membuat draf email lengkap dengan subjek *"Schedule for Next Week's Marketing Meeting"* seperti yang diinstruksikan oleh prompt sistemnya.
- **`open-code`**, **`pizza-orderer`**, **`stockbroker`**, **`trip-planner`**, **`writer-agent`**: Sukses dijalankan tanpa error. Seluruh agen tersebut meminta input parameter lebih spesifik sebelum menjalankan *tools* sesuai dengan arsitektur graf masing-masing.

### 4.2 Kendala Eksekusi pada Supervisor Agent
Satu agen, yakni **`supervisor`**, mengalami error pada saat dijalankan:
- **Error log**: `openai.BadRequestError: Error code: 400 - {'error': {'message': 'invalid model ID'...}}`
- **Penyebab**: Pada `output_files/langgraph/supervisor/main.py`, secara bawaan (*default*) disematkan `LLM_MODEL = "anthropic/claude-3-7-sonnet-latest"`, padahal klien LLM yang digunakan di dalam skrip adalah `ChatOpenAI`. Akibatnya OpenAI menolak *model ID* milik Anthropic tersebut. 
- **Tindak Lanjut**: Melakukan koreksi mapping *Model ID* dari *Knowledge Graph* agar bersesuaian dengan tipe provider LLM (seperti LangChain `ChatOpenAI` atau `ChatAnthropic`).

## 5. Kesimpulan dan Langkah Selanjutnya
Secara keseluruhan, *generator* kode LangGraph telah bekerja melampaui ekspektasi dasar. Tidak hanya berhasil memetakan *nodes* dan *tools* ke struktur StateGraph, namun kode yang dihasilkan **benar-benar dapat dieksekusi secara native** (executable) dan terhubung dengan API LLM secara sempurna. 

**Rencana Lanjutan**:
1. Memperbaiki format sintaks RDF pada file `utils_instances.ttl`.
2. Menyempurnakan pemetaan parameter `LLM_MODEL` agar sesuai dengan library providernya, terutama terkait kasus Anthropic/OpenAI pada agen `supervisor`.
3. Melanjutkan konversi framework *multi-agent* lain (seperti Mastra, CrewAI, AutoGen) sesuai dengan dokumen *Plan*.
