db.users.find({ age: { $gte: 18, $lte: 65 } }).explain('executionStats')
{
  explainVersion: '2',
  queryPlanner: {
    namespace: 'demodb.users',
    indexFilterSet: false,
    parsedQuery: {
      '$and': [ { age: { '$lte': 65 } }, { age: { '$gte': 18 } } ]
    },
    queryHash: '29EFE2BD',
    planCacheKey: 'D163D59A',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      queryPlan: {
        stage: 'FETCH',
        planNodeId: 2,
        inputStage: {
          stage: 'IXSCAN',
          planNodeId: 1,
          keyPattern: { age: 1, username: 1 },
          indexName: 'age_username_idx',
          isMultiKey: false,
          multiKeyPaths: { age: [], username: [] },
          isUnique: false,
          isSparse: false,
          isPartial: false,
          indexVersion: 2,
          direction: 'forward',
          indexBounds: { age: [ '[18, 65]' ], username: [ '[MinKey, MaxKey]' ] }
        }
      },
      slotBasedPlan: {
        slots: '$$RESULT=s11 env: { s2 = Nothing (SEARCH_META), s10 = {"age" : 1, "username" : 1}, s1 = TimeZoneDatabase(Europe/Copenhagen...Asia/Dushanbe) (timeZoneDB), s5 = KS(2B240A0104), s6 = KS(2B82F0FE04), s3 = 1704075299177 (NOW) }',
        stages: '[2] nlj inner [] [s4, s7, s8, s9, s10] \n' +
          '    left \n' +
          '        [1] cfilter {(exists(s5) && exists(s6))} \n' +
          '        [1] ixseek s5 s6 s9 s4 s7 s8 [] @"8429cf51-4b7f-4532-8a7d-f8592177cc1e" @"age_username_idx" true \n' +
          '    right \n' +
          '        [2] limit 1 \n' +
          '        [2] seek s4 s11 s12 s7 s8 s9 s10 [] @"8429cf51-4b7f-4532-8a7d-f8592177cc1e" true false \n'
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 762394,
    executionTimeMillis: 1819,
    totalKeysExamined: 762394,
    totalDocsExamined: 762394,
    executionStages: {
      stage: 'nlj',
      planNodeId: 2,
      nReturned: 762394,
      executionTimeMillisEstimate: 1817,
      opens: 1,
      closes: 1,
      saveState: 781,
      restoreState: 781,
      isEOF: 1,
      totalDocsExamined: 762394,
      totalKeysExamined: 762394,
      collectionScans: 0,
      collectionSeeks: 762394,
      indexScans: 0,
      indexSeeks: 1,
      indexesUsed: [ 'age_username_idx' ],
      innerOpens: 762394,
      innerCloses: 1,
      outerProjects: [],
      outerCorrelated: [ Long('4'), Long('7'), Long('8'), Long('9'), Long('10') ],
      outerStage: {
        stage: 'cfilter',
        planNodeId: 1,
        nReturned: 762394,
        executionTimeMillisEstimate: 1268,
        opens: 1,
        closes: 1,
        saveState: 781,
        restoreState: 781,
        isEOF: 1,
        numTested: 1,
        filter: '(exists(s5) && exists(s6)) ',
        inputStage: {
          stage: 'ixseek',
          planNodeId: 1,
          nReturned: 762394,
          executionTimeMillisEstimate: 1268,
          opens: 1,
          closes: 1,
          saveState: 781,
          restoreState: 781,
          isEOF: 1,
          indexName: 'age_username_idx',
          keysExamined: 762394,
          seeks: 1,
          numReads: 762395,
          indexKeySlot: 9,
          recordIdSlot: 4,
          snapshotIdSlot: 7,
          indexIdentSlot: 8,
          outputSlots: [],
          indexKeysToInclude: '00000000000000000000000000000000',
          seekKeyLow: 's5 ',
          seekKeyHigh: 's6 '
        }
      },
      innerStage: {
        stage: 'limit',
        planNodeId: 2,
        nReturned: 762394,
        executionTimeMillisEstimate: 547,
        opens: 762394,
        closes: 1,
        saveState: 781,
        restoreState: 781,
        isEOF: 1,
        limit: 1,
        inputStage: {
          stage: 'seek',
          planNodeId: 2,
          nReturned: 762394,
          executionTimeMillisEstimate: 547,
          opens: 762394,
          closes: 1,
          saveState: 781,
          restoreState: 781,
          isEOF: 0,
          numReads: 762394,
          recordSlot: 11,
          recordIdSlot: 12,
          seekKeySlot: 4,
          snapshotIdSlot: 7,
          indexIdentSlot: 8,
          indexKeySlot: 9,
          indexKeyPatternSlot: 10,
          fields: [],
          outputSlots: []
        }
      }
    }
  },
  command: {
    find: 'users',
    filter: { age: { '$gte': 18, '$lte': 65 } },
    '$db': 'demodb'
  },
  serverInfo: {
    host: '0bd36c90b0c0',
    port: 27017,
    version: '7.0.4',
    gitVersion: '38f3e37057a43d2e9f41a39142681a76062d582e'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeEngine'
  },
  ok: 1
}