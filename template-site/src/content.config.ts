import { defineCollection, z } from 'astro:content';

const concept = defineCollection({
  type: 'content',
  schema: z.object({
    slug: z.string(),
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
    slug: z.string(),
    title: z.string(),
    platform: z.enum(['youtube', 'bilibili']),
    source_url: z.string(),
    lecture_count: z.number(),
  }),
});

const lecture = defineCollection({
  type: 'content',
  schema: z.object({
    slug: z.string(),
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
