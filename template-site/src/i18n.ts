/**
 * Site UI i18n.
 *
 * Language is read from `import.meta.env.PUBLIC_LANGUAGE` (set by the
 * Python `video-to-notebook build` command from build_meta.language).
 * Falls back to 'zh' if unset (legacy projects).
 *
 * Usage in a .astro file:
 *   ---
 *   import { t } from '../i18n';
 *   ---
 *   <h1>{t.textbook_toc}</h1>
 *
 * Add a new string: add a `key: string` to the `Dict` type, then a
 * value in BOTH `dictZh` and `dictEn`. TypeScript will yell if either
 * is missing.
 */

export type Lang = 'zh' | 'en';

export interface Dict {
  // Nav
  nav_home: string;
  nav_textbook: string;
  nav_courses: string;
  nav_concepts: string;
  nav_about: string;
  nav_toggle_theme: string;
  // Index page
  index_lead: string;
  index_cta_open_textbook: string;
  index_stats: (courses: number, concepts: number) => string;
  index_browse_by_course: string;
  index_browse_by_concept: string;
  // Textbook
  textbook_toc: string;
  textbook_empty: string;
  textbook_empty_hint_html: string;
  textbook_progress: (done: number, total: number) => string;
  // Chapter nav
  chapter_prev: string;
  chapter_next: string;
  chapter_kbd_switch_hint: string;
  // Concepts
  concepts_encyclopedia: string;
  concepts_count_stats: (count: number) => string;
  concepts_blurb: string;
  concept_eyebrow: string;
  concept_breadcrumb_index: string;
  concept_no_explainer_title: string;
  concept_no_explainer_intro: string;
  concept_no_explainer_bullet_intuition: string;
  concept_no_explainer_bullet_svg: string;
  concept_no_explainer_bullet_example: string;
  concept_no_explainer_bullet_pitfalls: string;
  concept_no_explainer_bullet_seealso: string;
  concept_meta_slug: string;
  concept_meta_source: string;
  concept_meta_aliases: string;
  concept_meta_occurrences: string;
  concept_breadcrumb_aria: string;
  concept_pending_cli_label: string;
  concept_compare_link: (courseCount: number) => string;
  concept_source_count_summary: (count: number) => string;
  // Courses
  courses_all_title: string;
  courses_lecture_count_suffix: string;
  // About
  about_title: string;
  about_intro_html: string;
  about_stats_heading: string;
  about_stat_courses: (n: number) => string;
  about_stat_lectures: (n: number) => string;
  about_stat_chunks: (n: number) => string;
  about_stat_concepts: (n: number) => string;
  about_built_at: (iso: string) => string;
  // Search
  search_placeholder_loading: string;
}

export const dictZh: Dict = {
  nav_home: '首页',
  nav_textbook: '教材',
  nav_courses: '课程',
  nav_concepts: '概念',
  nav_about: '关于',
  nav_toggle_theme: '切换主题',
  index_lead: '把多门公开课合并成一本可读的教材。',
  index_cta_open_textbook: '进入教材目录 →',
  index_stats: (c, k) => `${c} 门课程 · ${k} 个概念已索引。`,
  index_browse_by_course: '按课程浏览',
  index_browse_by_concept: '按概念浏览',
  textbook_toc: '教材目录',
  textbook_empty: '暂无课程内容。',
  textbook_empty_hint_html:
    '先运行 <code>video-to-notebook curriculum --apply-results &lt;file&gt;</code> 设计目录，再运行 <code>video-to-notebook synthesize</code> 生成章节。',
  textbook_progress: (d, t) => `${d} / ${t} 章已生成`,
  chapter_prev: '← 上一章',
  chapter_next: '下一章 →',
  chapter_kbd_switch_hint: '切换章节',
  concepts_encyclopedia: '概念百科',
  concepts_count_stats: (n) => `${n} 个概念 ·`,
  concepts_blurb:
    '每个概念都是一份独立的图文解释：直觉 → 公式 → 图示 → 动画 → 例题 → 常见误区。',
  concept_eyebrow: '概念',
  concept_breadcrumb_index: '概念百科',
  concept_no_explainer_title: '这个概念暂时还没有详细解释。我们正在编写图文教程，包括：',
  concept_no_explainer_intro: '',
  concept_no_explainer_bullet_intuition: '📐 直觉与定义（生活类比 + 形式化表达）',
  concept_no_explainer_bullet_svg: '🎨 SVG 图示 + 动画演示',
  concept_no_explainer_bullet_example: '🧮 手算示例',
  concept_no_explainer_bullet_pitfalls: '⚠️ 常见误区',
  concept_no_explainer_bullet_seealso: '🔗 相关概念交叉链接',
  concept_meta_slug: '概念 slug',
  concept_meta_source: '来源',
  concept_meta_aliases: '别名',
  concept_meta_occurrences: '出现次数',
  concept_breadcrumb_aria: '面包屑',
  concept_pending_cli_label: 'CLI 生成命令：',
  concept_compare_link: (cc) => `跨课程对比 (${cc} 门) →`,
  concept_source_count_summary: (n) => `查看 ${n} 条课程原文出处`,
  courses_all_title: '全部课程',
  courses_lecture_count_suffix: '节课',
  about_title: '关于本站',
  about_intro_html:
    '本站由 <a href="https://github.com/LinZhuoChen/video-to-notebook">video-to-notebook</a> 生成 —— 抓取公开课、用 Claude 打概念标签、跨课程渲染概念页。',
  about_stats_heading: '统计',
  about_stat_courses: (n) => `${n} 门课程`,
  about_stat_lectures: (n) => `${n} 节课`,
  about_stat_chunks: (n) => `${n} 个 chunk`,
  about_stat_concepts: (n) => `${n} 个概念`,
  about_built_at: (iso) => `构建于 ${iso}`,
  search_placeholder_loading: '搜索 (先构建)…',
};

export const dictEn: Dict = {
  nav_home: 'Home',
  nav_textbook: 'Textbook',
  nav_courses: 'Courses',
  nav_concepts: 'Concepts',
  nav_about: 'About',
  nav_toggle_theme: 'Toggle theme',
  index_lead: 'Multiple open courses merged into one readable textbook.',
  index_cta_open_textbook: 'Open textbook contents →',
  index_stats: (c, k) => `${c} courses · ${k} concepts indexed.`,
  index_browse_by_course: 'Browse by course',
  index_browse_by_concept: 'Browse by concept',
  textbook_toc: 'Textbook contents',
  textbook_empty: 'No textbook content yet.',
  textbook_empty_hint_html:
    'Run <code>video-to-notebook curriculum --apply-results &lt;file&gt;</code> to design the table of contents, then <code>video-to-notebook synthesize</code> to generate each chapter.',
  textbook_progress: (d, t) => `${d} / ${t} chapters generated`,
  chapter_prev: '← Previous',
  chapter_next: 'Next →',
  chapter_kbd_switch_hint: 'navigate chapters',
  concepts_encyclopedia: 'Concept encyclopedia',
  concepts_count_stats: (n) => `${n} concepts ·`,
  concepts_blurb:
    'Each concept gets a self-contained illustrated entry: intuition → formula → diagram → animation → worked example → common pitfalls.',
  concept_eyebrow: 'Concept',
  concept_breadcrumb_index: 'Concept encyclopedia',
  concept_no_explainer_title:
    'No detailed explainer yet. We will publish one covering:',
  concept_no_explainer_intro: '',
  concept_no_explainer_bullet_intuition:
    '📐 Intuition & definition (everyday analogy + formal expression)',
  concept_no_explainer_bullet_svg: '🎨 SVG diagrams + animations',
  concept_no_explainer_bullet_example: '🧮 Worked numerical example',
  concept_no_explainer_bullet_pitfalls: '⚠️ Common misconceptions',
  concept_no_explainer_bullet_seealso: '🔗 Cross-links to related concepts',
  concept_meta_slug: 'Concept slug',
  concept_meta_source: 'Source',
  concept_meta_aliases: 'Aliases',
  concept_meta_occurrences: 'Occurrences',
  concept_breadcrumb_aria: 'breadcrumb',
  concept_pending_cli_label: 'CLI command:',
  concept_compare_link: (cc) => `Cross-course comparison (${cc}) →`,
  concept_source_count_summary: (n) => `Show ${n} source-clip references`,
  courses_all_title: 'All courses',
  courses_lecture_count_suffix: 'lectures',
  about_title: 'About this site',
  about_intro_html:
    'This site was generated by <a href="https://github.com/LinZhuoChen/video-to-notebook">video-to-notebook</a> — it crawls open-courseware, tags it with Claude, and renders cross-course concept pages.',
  about_stats_heading: 'Stats',
  about_stat_courses: (n) => `${n} courses`,
  about_stat_lectures: (n) => `${n} lectures`,
  about_stat_chunks: (n) => `${n} chunks`,
  about_stat_concepts: (n) => `${n} concepts`,
  about_built_at: (iso) => `Built at ${iso}`,
  search_placeholder_loading: 'Search (build first)…',
};

const lang: Lang =
  (import.meta.env.PUBLIC_LANGUAGE as Lang) === 'en' ? 'en' : 'zh';

export const t: Dict = lang === 'en' ? dictEn : dictZh;
export const currentLanguage: Lang = lang;
