-- Lead magnets de LA REAL: base propia de contactos y plata por lead magnet.
create table if not exists public.admins (email text primary key check (email = lower(email)));

create table if not exists public.lead_magnets (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique check (slug ~ '^[a-z0-9-]{2,60}$'),
  nombre text not null check (char_length(nombre) between 2 and 160),
  palabra_clave text check (char_length(palabra_clave) <= 40),
  url_recurso text check (char_length(url_recurso) <= 500),
  activo boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists public.leads (
  id uuid primary key default gen_random_uuid(),
  lead_magnet_id uuid not null references public.lead_magnets(id),
  email text not null check (email = lower(email) and email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' and char_length(email) <= 200),
  nombre text check (char_length(nombre) <= 120),
  whatsapp text check (char_length(whatsapp) <= 40),
  tienda_url text check (char_length(tienda_url) <= 300),
  utm_source text check (char_length(utm_source) <= 120),
  utm_medium text check (char_length(utm_medium) <= 120),
  utm_campaign text check (char_length(utm_campaign) <= 120),
  created_at timestamptz not null default now(),
  unique (lead_magnet_id, email)
);
create index if not exists leads_email_idx on public.leads (email);

-- Plata que dejó un contacto. Se suma al lead magnet por el que entró.
create table if not exists public.ingresos (
  id uuid primary key default gen_random_uuid(),
  lead_id uuid not null references public.leads(id) on delete cascade,
  monto numeric(14,2) not null check (monto > 0),
  moneda text not null default 'COP' check (moneda in ('COP','USD')),
  fecha date not null default current_date,
  concepto text check (char_length(concepto) <= 200),
  created_at timestamptz not null default now()
);
create index if not exists ingresos_lead_idx on public.ingresos (lead_id);

create or replace function public.es_admin() returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.admins a where a.email = lower((select auth.jwt() ->> 'email')));
$$;
revoke all on function public.es_admin() from public, anon;
grant execute on function public.es_admin() to authenticated;

alter table public.admins enable row level security;
alter table public.lead_magnets enable row level security;
alter table public.leads enable row level security;
alter table public.ingresos enable row level security;

-- Visitantes: solo ven los lead magnets activos y solo pueden dejar sus datos. No leen contactos.
create policy "publico ve lead magnets activos" on public.lead_magnets for select to anon using (activo);
create policy "publico se registra" on public.leads for insert to anon, authenticated with check (true);

-- Admin: todo.
create policy "admin lee admins" on public.admins for select to authenticated using ((select public.es_admin()));
create policy "admin lead magnets" on public.lead_magnets for all to authenticated using ((select public.es_admin())) with check ((select public.es_admin()));
create policy "admin lee leads" on public.leads for select to authenticated using ((select public.es_admin()));
create policy "admin borra leads" on public.leads for delete to authenticated using ((select public.es_admin()));
create policy "admin ingresos" on public.ingresos for all to authenticated using ((select public.es_admin())) with check ((select public.es_admin()));

-- 23 nov 2026: consentimiento para recibir ideas y ofertas por email (casilla marcada por defecto en /cross)
alter table public.leads
  add column if not exists acepta_ofertas boolean not null default false,
  add column if not exists consentimiento_texto text check (consentimiento_texto is null or length(consentimiento_texto) <= 500);
