import { defineCollection, z } from 'astro:content';

// Note: Astro 5 reserves `slug` for the auto-generated filename slug.
// We use `entry.slug` directly in pages — do NOT redeclare slug in the schema.

const concept = defineCollection({
  type: 'content',
  schema: z.object({
    canonical_name: z.string(),
    description: z.string().default(''),
    ontology_source: z.enum(['seed', 'discovered', 'user']),
    aliases: z.array(z.string()).default([]),
    occurrence_count: z.number().default(0),
  }),
});

const course = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    platform: z.enum(['youtube', 'bilibili']),
    source_url: z.string(),
    lecture_count: z.number(),
  }),
});

const lecture = defineCollection({
  type: 'content',
  schema: z.object({
    course_slug: z.string(),
    idx: z.number(),
    title: z.string(),
    video_url: z.string(),
    duration_sec: z.number().nullable().default(null),
    chunks: z.array(z.object({
      idx: z.number(),
      start_sec: z.number(),
      end_sec: z.number(),
      text: z.string(),
      concept_slugs: z.array(z.string()).default([]),
    })),
  }),
});

export const collections = { concept, course, lecture };
